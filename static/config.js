// Configuration file for Skycast
// Replace the values below with your actual credentials

const CONFIG = {
    // Google OAuth Configuration
    // Get this from Google Cloud Console > APIs & Services > Credentials
    GOOGLE_CLIENT_ID: 'DEMO_CLIENT_ID', // Replace with your actual Google OAuth client ID
    
    // App Configuration
    APP_NAME: 'Skycast',
    APP_VERSION: '1.0.0',
    
    // API Configuration (for future use)
    API_BASE_URL: window.location.origin,
    
    // Feature Flags
    FEATURES: {
        GOOGLE_SIGNIN: false, // Will be automatically enabled when valid client ID is provided
        EMAIL_SIGNUP: true,
        WEATHER_FORECAST: true,
        USER_PROFILES: true
    }
};

// Auto-detect if Google Sign-In should be enabled
if (CONFIG.GOOGLE_CLIENT_ID && CONFIG.GOOGLE_CLIENT_ID !== 'DEMO_CLIENT_ID') {
    CONFIG.FEATURES.GOOGLE_SIGNIN = true;
}

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CONFIG;
} else {
    window.CONFIG = CONFIG;
}
