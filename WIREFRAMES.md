# Skycast - Wireframes & UI Documentation

## Project Overview
Skycast is a modern, AI-powered weather prediction application featuring machine learning-based forecasting, user authentication, and a beautiful glassmorphism UI design.

---

## 📱 Page Structure & Wireframes

### 1. Landing Page (`/`)
```
┌─────────────────────────────────────────────────────────────┐
│                        HEADER                               │
│  🌤️ Skycast    [Home] [About] [Contact] [Sign In] │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                      HERO SECTION                          │
│              🌍 Weather Prediction for Ghana                │
│         Advanced AI-powered forecasting system             │
│                                                             │
│              [Get Weather Forecast] (CTA Button)           │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                   QUICK FORECAST WIDGET                    │
│  ┌─────────────────┐ ┌──────────────┐ ┌─────────────────┐  │
│  │ 📍 Select City  │ │ Duration ⏰  │ │ [Check Weather] │  │
│  │ [Dropdown]      │ │ [Dropdown]   │ │                 │  │
│  └─────────────────┘ └──────────────┘ └─────────────────┘  │
├─────────────────────────────────────────────────────────────┤
│                      FOOTER                                 │
│              © 2025 Skycast                      │
└─────────────────────────────────────────────────────────────┘
```

### 2. Advanced Forecast Page (Modal/Popup)
```
┌─────────────────────────────────────────────────────────────┐
│                    ADVANCED FORECAST                        │
│                                                        [×]  │
├─────────────────────────────────────────────────────────────┤
│  LOCATION SEARCH                                            │
│  ┌─────────────────────────────────────────────────────────┐│
│  │ 🔍 Search city or coordinates...                       ││
│  └─────────────────────────────────────────────────────────┘│
│  [📍 Use My Location] [🗺️ Select on Map]                   │
│                                                             │
│  DATE & TIME FILTERS                                        │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────────────┐│
│  │ Start Date   │ │ End Date     │ │ Time of Day          ││
│  │ [Date Picker]│ │ [Date Picker]│ │ [Morning/Afternoon/  ││
│  │              │ │              │ │  Evening/Night]      ││
│  └──────────────┘ └──────────────┘ └──────────────────────┘│
│                                                             │
│  MODEL & UNITS                                              │
│  ┌──────────────────┐ ┌────────────────────────────────────┐│
│  │ Model Type       │ │ Units                              ││
│  │ [Enhanced/Basic] │ │ [Celsius/Fahrenheit] [km/h/mph]   ││
│  └──────────────────┘ └────────────────────────────────────┘│
│                                                             │
│                    [Generate Forecast]                     │
└─────────────────────────────────────────────────────────────┘
```

### 3. Weather Results (Modal/Popup)
```
┌─────────────────────────────────────────────────────────────┐
│                    WEATHER FORECAST                         │
│                                                        [×]  │
├─────────────────────────────────────────────────────────────┤
│  CURRENT WEATHER SUMMARY                                    │
│  ┌─────────────────────────────────────────────────────────┐│
│  │ 🌤️ Accra, Ghana                          🌡️ 28°C      ││
│  │ Partly Cloudy                            💧 65% Humidity││
│  │ Feels like 31°C                          💨 12 km/h    ││
│  └─────────────────────────────────────────────────────────┘│
│                                                             │
│  FORECAST TIMELINE                                          │
│  ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────────┐│
│  │Today│ +1  │ +2  │ +3  │ +4  │ +5  │ +6  │ +7  │   ...   ││
│  │ 28° │ 29° │ 27° │ 26° │ 30° │ 31° │ 29° │ 28° │         ││
│  │ ☀️  │ ⛅  │ 🌧️  │ ⛈️  │ ☀️  │ ☀️  │ ⛅  │ 🌤️  │         ││
│  └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────────┘│
│                                                             │
│  DETAILED CHARTS                                            │
│  ┌─────────────────────────────────────────────────────────┐│
│  │     Temperature Trend Chart                            ││
│  │  35°┤                                                  ││
│  │  30°┤     ●─●─●                                        ││
│  │  25°┤   ●         ●─●─●                                ││
│  │  20°┤ ●                                                ││
│  │     └─────────────────────────────────────────────────  ││
│  └─────────────────────────────────────────────────────────┘│
│                                                             │
│  MODEL CONFIDENCE: ████████░░ 85%                          │
│                                                             │
│  [📤 Share] [💾 Save] [📊 Detailed View]                   │
└─────────────────────────────────────────────────────────────┘
```

### 4. Authentication Modals

#### Login Modal
```
┌─────────────────────────────────────────────────────────────┐
│                      SIGN IN                           [×]  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────────┐│
│  │ 📧 Email Address                                       ││
│  │ [email@example.com                                   ] ││
│  └─────────────────────────────────────────────────────────┘│
│                                                             │
│  ┌─────────────────────────────────────────────────────────┐│
│  │ 🔒 Password                                            ││
│  │ [••••••••••••••••••••••••••••••••••••••••••••••••••] ││
│  └─────────────────────────────────────────────────────────┘│
│                                                             │
│                    [Sign In]                               │
│                                                             │
│  ─────────────────── OR ───────────────────                │
│                                                             │
│  ┌─────────────────────────────────────────────────────────┐│
│  │ 🔵 Continue with Google (Demo)                         ││
│  └─────────────────────────────────────────────────────────┘│
│                                                             │
│  Don't have an account? [Sign Up]                          │
│  [Forgot Password?]                                         │
└─────────────────────────────────────────────────────────────┘
```

#### Signup Modal
```
┌─────────────────────────────────────────────────────────────┐
│                     SIGN UP                            [×]  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────────┐│
│  │ 👤 Full Name                                           ││
│  │ [John Doe                                            ] ││
│  └─────────────────────────────────────────────────────────┘│
│                                                             │
│  ┌─────────────────────────────────────────────────────────┐│
│  │ 📧 Email Address                                       ││
│  │ [john@example.com                                    ] ││
│  └─────────────────────────────────────────────────────────┘│
│                                                             │
│  ┌─────────────────────────────────────────────────────────┐│
│  │ 🔒 Password                                            ││
│  │ [••••••••••••••••••••••••••••••••••••••••••••••••••] ││
│  └─────────────────────────────────────────────────────────┘│
│                                                             │
│  ┌─────────────────────────────────────────────────────────┐│
│  │ 🔒 Confirm Password                                    ││
│  │ [••••••••••••••••••••••••••••••••••••••••••••••••••] ││
│  └─────────────────────────────────────────────────────────┘│
│                                                             │
│                   [Create Account]                         │
│                                                             │
│  ─────────────────── OR ───────────────────                │
│                                                             │
│  ┌─────────────────────────────────────────────────────────┐│
│  │ 🔵 Continue with Google (Demo)                         ││
│  └─────────────────────────────────────────────────────────┘│
│                                                             │
│  Already have an account? [Sign In]                        │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎨 Design System

### Color Palette
- **Primary Background**: `#0a0a0a` (Deep Black)
- **Secondary Background**: `#1a1a1a` (Dark Gray)
- **Glass Elements**: `rgba(255, 255, 255, 0.1)` with backdrop blur
- **Text Primary**: `#ffffff` (White)
- **Text Secondary**: `#b0b0b0` (Light Gray)
- **Accent Blue**: `#3b82f6` (Primary CTA)
- **Success Green**: `#10b981`
- **Warning Orange**: `#f59e0b`
- **Error Red**: `#ef4444`

### Typography
- **Headings**: Inter, Bold (700)
- **Body Text**: Inter, Regular (400)
- **Buttons**: Inter, Medium (500)
- **Captions**: Inter, Light (300)

### Glassmorphism Effects
- **Background**: `rgba(255, 255, 255, 0.1)`
- **Backdrop Filter**: `blur(10px)`
- **Border**: `1px solid rgba(255, 255, 255, 0.2)`
- **Border Radius**: `16px`
- **Box Shadow**: `0 8px 32px rgba(0, 0, 0, 0.3)`

---

## 📱 Responsive Breakpoints

### Desktop (1200px+)
- Full sidebar navigation
- Multi-column layouts
- Large modal dialogs
- Expanded forecast cards

### Tablet (768px - 1199px)
- Collapsible navigation
- Two-column layouts
- Medium modal dialogs
- Stacked forecast cards

### Mobile (320px - 767px)
- Hamburger menu navigation
- Single-column layouts
- Full-screen modals
- Vertical forecast timeline
- Touch-optimized buttons

---

## 🔄 User Flow Diagrams

### Authentication Flow
```
Landing Page
     │
     ├─→ Click "Sign In"
     │   │
     │   ├─→ Email Login → Success → Dashboard
     │   │
     │   └─→ Google Login → Success → Dashboard
     │
     └─→ Click "Sign Up"
         │
         ├─→ Email Signup → Success → Auto Login → Dashboard
         │
         └─→ Google Signup → Success → Auto Login → Dashboard
```

### Weather Forecast Flow
```
Landing Page
     │
     ├─→ Quick Forecast Widget
     │   │
     │   └─→ Select City + Duration → Results Modal
     │
     └─→ Advanced Forecast Button
         │
         └─→ Advanced Options Modal
             │
             └─→ Configure Options → Results Modal
                 │
                 ├─→ Share Results
                 ├─→ Save to Profile
                 └─→ View Detailed Charts
```

---

## 🎯 Key Features Highlighted

### ✅ Implemented Features
- **Modern Landing Page** with hero section and quick forecast
- **Advanced Forecast Input** with location search, date filters, model options
- **Weather Results Modal** with summary, timeline, and confidence meter
- **Complete Authentication** with email signup/login and Google OAuth demo
- **Responsive Design** with glassmorphism and dark theme
- **User Session Management** with personalized navigation

### 🚧 Planned Features
- **User Dashboard** with saved locations and forecast history
- **Notification Settings** for weather alerts
- **Forecast Sharing** via social media and export options
- **Mobile Optimizations** with swipe gestures and GPS integration
- **Advanced Charts** with interactive weather data visualization

---

This wireframe documentation provides a complete overview of the Skycast application's UI structure, design system, and user experience flow.
