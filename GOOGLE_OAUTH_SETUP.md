# Google OAuth Setup Guide for Skycast

## Step-by-Step Instructions

### 1. Create Google Cloud Console Project

1. **Go to Google Cloud Console**: https://console.cloud.google.com/
2. **Sign in** with your Google account
3. **Create a new project**:
   - Click "Select a project" dropdown at the top
   - Click "NEW PROJECT"
   - Project name: `Skycast`
   - Click "CREATE"

### 2. Enable Google Sign-In API

1. **Navigate to APIs & Services**:
   - In the left sidebar, click "APIs & Services" > "Library"
2. **Search for Google Sign-In API**:
   - Search for "Google Identity"
   - Click on "Google Identity Toolkit API"
   - Click "ENABLE"

### 3. Configure OAuth Consent Screen

1. **Go to OAuth consent screen**:
   - Left sidebar: "APIs & Services" > "OAuth consent screen"
2. **Choose User Type**:
   - Select "External" (for public use)
   - Click "CREATE"
3. **Fill out App Information**:
   - App name: `Skycast`
   - User support email: `your-email@gmail.com`
   - Developer contact: `your-email@gmail.com`
   - Click "SAVE AND CONTINUE"
4. **Scopes** (click "SAVE AND CONTINUE")
5. **Test users** (click "SAVE AND CONTINUE")
6. **Summary** (click "BACK TO DASHBOARD")

### 4. Create OAuth Client ID

1. **Go to Credentials**:
   - Left sidebar: "APIs & Services" > "Credentials"
2. **Create Credentials**:
   - Click "CREATE CREDENTIALS" > "OAuth client ID"
3. **Configure OAuth Client**:
   - Application type: "Web application"
   - Name: `Skycast Web Client`
   - Authorized JavaScript origins:
     - `http://localhost:5000`
     - `http://127.0.0.1:5000`
     - Add your domain when you deploy (e.g., `https://yourdomain.com`)
   - Authorized redirect URIs: (leave empty for now)
   - Click "CREATE"

### 5. Copy Your Client ID

1. **Copy the Client ID** from the popup (it looks like: `123456789-abcdefghijklmnop.apps.googleusercontent.com`)
2. **Save it securely** - you'll need this for the next step

### 6. Update Your App

Once you have your Client ID, replace `DEMO_CLIENT_ID` in your `landing.html` file:

```javascript
const GOOGLE_CLIENT_ID = 'YOUR_ACTUAL_CLIENT_ID_HERE';
```

### 7. Test Google Sign-In

1. **Restart your Flask app**
2. **Open your weather app**
3. **Click "Sign In" or "Sign Up"**
4. **You should now see "Continue with Google" buttons**
5. **Test the Google Sign-In flow**

## Important Notes

- **Development**: Use `http://localhost:5000` for testing
- **Production**: Add your actual domain to authorized origins
- **Security**: Never commit your client ID to public repositories
- **Verification**: Google may require app verification for production use

## Troubleshooting

- **"Access blocked" error**: Check authorized JavaScript origins
- **"Invalid client" error**: Verify client ID is correct
- **Buttons not showing**: Check browser console for errors

## Support

If you encounter issues:
1. Check the browser console for errors
2. Verify all URLs in Google Cloud Console match your app
3. Ensure the Google Identity API is enabled
4. Try incognito/private browsing mode

---

**After completing these steps, your Google Sign-In will work perfectly with your Skycast app!**
