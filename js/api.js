/**
 * Go Backend Adapter for Deep AI System
 * Replaces Firebase SDK with native Fetch API calls to local Go Backend
 */

const API_BASE = '/api';

// --- Mock Firebase Auth ---
class MockAuth {
    constructor() {
        this.currentUser = { uid: "local-admin-" + Math.random().toString(36).substr(2, 9) };
        this.listeners = [];

        // Auto-trigger auth state
        setTimeout(() => {
            this.listeners.forEach(cb => cb(this.currentUser));
        }, 100);
    }

    onAuthStateChanged(callback) {
        this.listeners.push(callback);
        // Immediate callback if user exists
        if (this.currentUser) callback(this.currentUser);
    }

    async signInAnonymously() {
        return { user: this.currentUser };
    }
}

// --- Mock Firebase Database ---
class MockSnapshot {
    constructor(data) {
        this.data = data;
        this.key = null; // simplified
    }

    val() { return this.data; }
    exists() { return this.data !== null && this.data !== undefined; }
    numChildren() { return this.data ? Object.keys(this.data).length : 0; }

    forEach(action) {
        if (!this.data) return;
        Object.keys(this.data).forEach(key => {
            const childSnap = new MockSnapshot(this.data[key]);
            childSnap.key = key;
            action(childSnap);
        });
    }
}

class MockRef {
    constructor(path) {
        this.path = path;
        this.query = {};
    }

    // -- Query Modifiers --
    orderByChild(key) { this.query.orderBy = key; return this; }
    equalTo(val) { this.query.equalTo = val; return this; }
    limitToLast(n) { this.query.limitToLast = n; return this; }

    // -- Operations --
    _getEndpoint() {
        if (this.path === '.info/connected') return '/api/status';
        if (this.path === 'students_list') return '/api/students';
        if (this.path.startsWith('attendanceRecords')) return '/api/attendance';
        return '/api/' + this.path;
    }

    async _fetchData() {
        // Special case for connection check
        if (this.path === '.info/connected') {
            try {
                const res = await fetch(API_BASE + '/status');
                return res.ok;
            } catch { return false; }
        }

        const res = await fetch(API_BASE + this._getEndpoint());
        if (!res.ok) throw new Error(res.statusText);
        let data = await res.json();

        // Client-side filtering to match Firebase Query Logic
        if (this.query.orderBy && this.query.equalTo !== undefined) {
            const filtered = {};
            if (data) {
                Object.keys(data).forEach(k => {
                    if (data[k][this.query.orderBy] == this.query.equalTo) {
                        filtered[k] = data[k];
                    }
                });
            }
            data = filtered;
        }

        return data;
    }

    async once(eventType) {
        const data = await this._fetchData();
        return new MockSnapshot(data);
    }

    on(eventType, callback) {
        // Initial fetch
        this._fetchData().then(data => callback(new MockSnapshot(data)));

        // Polling loop
        this.interval = setInterval(async () => {
            try {
                const data = await this._fetchData();
                callback(new MockSnapshot(data));
            } catch (e) {
                console.error("Polling error:", e);
            }
        }, 3000); // Poll every 3 seconds
    }

    async set(data) {
        const res = await fetch(API_BASE + '/students', { // Hardcoded for simplified list set
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        if (!res.ok) throw new Error("Update failed");
    }

    async push(data) {
        // Sanitize ServerValue.TIMESTAMP
        if (data.timestamp && typeof data.timestamp === 'object') {
            data.timestamp = Date.now();
        }

        const res = await fetch(API_BASE + '/attendance', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        if (!res.ok) throw new Error("Push failed");
        return res.json(); // returns {name: "id"}
    }

    async remove() {
        // Path is like attendanceRecords/-N...
        // Extract ID
        const parts = this.path.split('/');
        const id = parts[parts.length - 1];

        const res = await fetch(API_BASE + '/attendance/' + id, { method: 'DELETE' });
        if (!res.ok) throw new Error("Delete failed");
    }
}

// Global Firebase Objects
const firebase = {
    apps: [],
    initializeApp: (config) => { firebase.apps.push(true); },
    auth: () => new MockAuth(),
    database: () => {
        return {
            ref: (path) => new MockRef(path),
            ServerValue: { TIMESTAMP: { '.sv': 'timestamp' } }
        };
    }
};

console.log("🚀 Deep AI: Go Backend Adapter Loaded");
