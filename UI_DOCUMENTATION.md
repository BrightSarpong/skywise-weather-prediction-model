# Skycast - UI Documentation

## 🎨 Complete UI Design System & Components

### Project Overview
Skycast is a modern weather prediction application featuring a sophisticated glassmorphism design, dark theme, and comprehensive authentication system. This documentation provides detailed specifications for all UI components and design patterns.

---

## 🎯 Design Philosophy

### Core Principles
- **Glassmorphism**: Translucent elements with backdrop blur effects
- **Dark Theme**: Professional dark color scheme for better visibility
- **Minimalism**: Clean, uncluttered interface focusing on essential information
- **Accessibility**: High contrast ratios and readable typography
- **Responsiveness**: Seamless experience across all device sizes

---

## 🎨 Visual Design System

### Color Palette

#### Primary Colors
```css
--bg-primary: #0a0a0a;           /* Deep black background */
--bg-secondary: #1a1a1a;         /* Secondary dark background */
--bg-tertiary: #2a2a2a;          /* Tertiary background for cards */
```

#### Glass Effects
```css
--glass-bg: rgba(255, 255, 255, 0.1);     /* Glass background */
--glass-border: rgba(255, 255, 255, 0.2);  /* Glass border */
--glass-hover: rgba(255, 255, 255, 0.15);  /* Glass hover state */
```

#### Text Colors
```css
--text-primary: #ffffff;         /* Primary white text */
--text-secondary: #b0b0b0;       /* Secondary gray text */
--text-muted: #808080;           /* Muted text for captions */
```

#### Accent Colors
```css
--accent-blue: #3b82f6;          /* Primary CTA buttons */
--accent-blue-hover: #2563eb;    /* Blue hover state */
--success-green: #10b981;        /* Success messages */
--warning-orange: #f59e0b;       /* Warning messages */
--error-red: #ef4444;            /* Error messages */
```

### Typography Scale

#### Font Family
```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

#### Font Weights & Sizes
```css
/* Headings */
--h1-size: 3rem;     /* 48px */ --h1-weight: 700;
--h2-size: 2.5rem;   /* 40px */ --h2-weight: 600;
--h3-size: 2rem;     /* 32px */ --h3-weight: 600;
--h4-size: 1.5rem;   /* 24px */ --h4-weight: 500;

/* Body Text */
--body-large: 1.125rem;  /* 18px */ --body-weight: 400;
--body-normal: 1rem;     /* 16px */ --body-weight: 400;
--body-small: 0.875rem;  /* 14px */ --body-weight: 400;

/* UI Elements */
--button-text: 1rem;     /* 16px */ --button-weight: 500;
--caption: 0.75rem;      /* 12px */ --caption-weight: 400;
```

### Spacing System
```css
--space-xs: 0.25rem;    /* 4px */
--space-sm: 0.5rem;     /* 8px */
--space-md: 1rem;       /* 16px */
--space-lg: 1.5rem;     /* 24px */
--space-xl: 2rem;       /* 32px */
--space-2xl: 3rem;      /* 48px */
--space-3xl: 4rem;      /* 64px */
```

### Border Radius
```css
--radius-sm: 8px;       /* Small elements */
--radius-md: 12px;      /* Medium elements */
--radius-lg: 16px;      /* Large cards/modals */
--radius-xl: 24px;      /* Hero sections */
--radius-full: 9999px;  /* Pills/badges */
```

---

## 🧩 Component Library

### 1. Navigation Header

#### Desktop Navigation
```html
<header class="glass-header">
  <div class="nav-brand">
    <span class="weather-icon">🌤️</span>
    <span class="brand-text">Skycast</span>
  </div>
  <nav class="nav-links">
    <a href="#home">Home</a>
    <a href="#about">About</a>
    <a href="#contact">Contact</a>
  </nav>
  <div class="nav-auth">
    <button class="btn-secondary">Sign In</button>
  </div>
</header>
```

#### Styling
```css
.glass-header {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
  padding: 1rem 2rem;
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 1000;
}
```

### 2. Hero Section

#### Structure
```html
<section class="hero-section">
  <div class="hero-content">
    <h1 class="hero-title">Weather Prediction for Ghana</h1>
    <p class="hero-subtitle">Advanced AI-powered forecasting system</p>
    <button class="btn-primary hero-cta">Get Weather Forecast</button>
  </div>
  <div class="hero-background">
    <!-- Animated weather elements -->
  </div>
</section>
```

#### Styling
```css
.hero-section {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
  position: relative;
  overflow: hidden;
}

.hero-title {
  font-size: 3.5rem;
  font-weight: 700;
  background: linear-gradient(135deg, #ffffff 0%, #b0b0b0 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 1rem;
}
```

### 3. Glass Cards

#### Basic Glass Card
```html
<div class="glass-card">
  <div class="card-header">
    <h3 class="card-title">Card Title</h3>
  </div>
  <div class="card-content">
    <p>Card content goes here...</p>
  </div>
</div>
```

#### Styling
```css
.glass-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
  transition: all 0.3s ease;
}

.glass-card:hover {
  background: rgba(255, 255, 255, 0.15);
  transform: translateY(-2px);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
}
```

### 4. Button Components

#### Primary Button
```css
.btn-primary {
  background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
  color: white;
  border: none;
  border-radius: 12px;
  padding: 0.75rem 1.5rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-primary:hover {
  background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
  transform: translateY(-1px);
  box-shadow: 0 8px 25px rgba(59, 130, 246, 0.3);
}
```

#### Secondary Button
```css
.btn-secondary {
  background: rgba(255, 255, 255, 0.1);
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  padding: 0.75rem 1.5rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.2);
  border-color: rgba(255, 255, 255, 0.3);
}
```

#### Google Sign-In Button
```css
.google-signin-btn {
  background: white;
  color: #1f2937;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  padding: 0.75rem 1rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
}

.google-signin-btn:hover {
  background: #f9fafb;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}
```

### 5. Form Elements

#### Input Fields
```css
.form-input {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  padding: 0.75rem 1rem;
  color: white;
  font-size: 1rem;
  width: 100%;
  transition: all 0.3s ease;
}

.form-input:focus {
  outline: none;
  border-color: #3b82f6;
  background: rgba(255, 255, 255, 0.15);
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.form-input::placeholder {
  color: rgba(255, 255, 255, 0.5);
}
```

#### Select Dropdowns
```css
.form-select {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  padding: 0.75rem 1rem;
  color: white;
  font-size: 1rem;
  cursor: pointer;
  appearance: none;
  background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2'%3e%3cpolyline points='6,9 12,15 18,9'%3e%3c/polyline%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-position: right 1rem center;
  background-size: 1rem;
}
```

### 6. Modal Components

#### Modal Structure
```html
<div class="modal-overlay">
  <div class="modal-container">
    <div class="modal-header">
      <h2 class="modal-title">Modal Title</h2>
      <button class="modal-close">×</button>
    </div>
    <div class="modal-content">
      <!-- Modal content -->
    </div>
  </div>
</div>
```

#### Modal Styling
```css
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2000;
}

.modal-container {
  background: rgba(26, 26, 26, 0.95);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 20px;
  max-width: 500px;
  width: 90%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
}
```

### 7. Notification System

#### Success Notification
```css
.notification-success {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  padding: 1rem 1.5rem;
  border-radius: 12px;
  box-shadow: 0 8px 25px rgba(16, 185, 129, 0.3);
  display: flex;
  align-items: center;
  gap: 0.75rem;
  animation: slideInRight 0.3s ease;
}
```

#### Error Notification
```css
.notification-error {
  background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
  color: white;
  padding: 1rem 1.5rem;
  border-radius: 12px;
  box-shadow: 0 8px 25px rgba(239, 68, 68, 0.3);
  display: flex;
  align-items: center;
  gap: 0.75rem;
  animation: slideInRight 0.3s ease;
}
```

---

## 📱 Responsive Design

### Breakpoint System
```css
/* Mobile First Approach */
@media (min-width: 640px) { /* sm */ }
@media (min-width: 768px) { /* md */ }
@media (min-width: 1024px) { /* lg */ }
@media (min-width: 1280px) { /* xl */ }
@media (min-width: 1536px) { /* 2xl */ }
```

### Mobile Optimizations
```css
@media (max-width: 767px) {
  .hero-title {
    font-size: 2.5rem;
  }
  
  .glass-card {
    padding: 1rem;
    border-radius: 12px;
  }
  
  .modal-container {
    width: 95%;
    margin: 1rem;
  }
  
  .btn-primary, .btn-secondary {
    width: 100%;
    padding: 1rem;
  }
}
```

---

## 🎭 Animation System

### Keyframe Animations
```css
@keyframes slideInRight {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes fadeInUp {
  from {
    transform: translateY(30px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}
```

### Transition Standards
```css
/* Standard transitions for interactive elements */
.interactive-element {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Hover effects */
.hover-lift:hover {
  transform: translateY(-2px);
}

.hover-scale:hover {
  transform: scale(1.05);
}
```

---

## 🔧 Implementation Guidelines

### CSS Architecture
1. **Base Styles**: Reset, typography, global variables
2. **Layout**: Grid systems, containers, spacing utilities
3. **Components**: Reusable UI components
4. **Utilities**: Helper classes for common patterns
5. **Responsive**: Media queries and mobile optimizations

### Performance Considerations
- **CSS Custom Properties**: Use for dynamic theming
- **Backdrop Filter**: Apply sparingly for performance
- **Animations**: Use `transform` and `opacity` for smooth animations
- **Critical CSS**: Inline critical styles for faster loading

### Accessibility Features
- **High Contrast**: Ensure 4.5:1 contrast ratio minimum
- **Focus States**: Visible focus indicators for keyboard navigation
- **Screen Readers**: Proper ARIA labels and semantic HTML
- **Touch Targets**: Minimum 44px touch target size

---

## 📊 Component Usage Examples

### Weather Card Component
```html
<div class="weather-card glass-card">
  <div class="weather-location">
    <span class="location-icon">📍</span>
    <span class="location-name">Accra, Ghana</span>
  </div>
  <div class="weather-main">
    <span class="weather-icon">🌤️</span>
    <span class="temperature">28°C</span>
  </div>
  <div class="weather-details">
    <div class="detail-item">
      <span class="detail-label">Humidity</span>
      <span class="detail-value">65%</span>
    </div>
    <div class="detail-item">
      <span class="detail-label">Wind</span>
      <span class="detail-value">12 km/h</span>
    </div>
  </div>
</div>
```

### Quick Forecast Widget
```html
<div class="quick-forecast glass-card">
  <h3 class="widget-title">Quick Forecast</h3>
  <div class="forecast-inputs">
    <select class="form-select city-select">
      <option>Select City</option>
      <option>Accra</option>
      <option>Kumasi</option>
      <option>Tamale</option>
    </select>
    <select class="form-select duration-select">
      <option>Duration</option>
      <option>Today</option>
      <option>3 Days</option>
      <option>7 Days</option>
    </select>
    <button class="btn-primary forecast-btn">Check Weather</button>
  </div>
</div>
```

---

This comprehensive UI documentation provides all the necessary specifications for implementing and maintaining the Skycast design system. Each component is designed to work harmoniously within the glassmorphism aesthetic while maintaining excellent usability and accessibility standards.