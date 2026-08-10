/**
 * HeartCheck DL - Client-side JavaScript
 * Handles form interactions, validations, and UI enhancements
 */

// Initialize on DOM load
document.addEventListener('DOMContentLoaded', function() {
    console.log('HeartCheck DL initialized');
    
    // Add smooth scroll behavior
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
    
    // Animate elements on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animation = 'fadeInUp 0.6s ease forwards';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    document.querySelectorAll('.feature-card, .stat-card').forEach(el => {
        observer.observe(el);
    });
});

// Form validation helpers
function validateAge(age) {
    return age >= 1 && age <= 120;
}

function validateBloodPressure(bp) {
    return bp >= 20 && bp <= 300;
}

function validateCholesterol(chol) {
    return chol >= 0 && chol <= 600;
}

function validateHeartRate(hr) {
    return hr >= 50 && hr <= 220;
}

function validateOldpeak(oldpeak) {
    return oldpeak >= 0 && oldpeak <= 10;
}

// Export for use in templates if needed
window.HeartCheckValidation = {
    validateAge,
    validateBloodPressure,
    validateCholesterol,
    validateHeartRate,
    validateOldpeak
};

// API helper for programmatic predictions
async function predictHeartRisk(patientData) {
    try {
        const response = await fetch('/api/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(patientData)
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Prediction failed');
        }
        
        return await response.json();
    } catch (error) {
        console.error('Prediction error:', error);
        throw error;
    }
}

// Health check
async function checkAPIHealth() {
    try {
        const response = await fetch('/api/health');
        const health = await response.json();
        console.log('API Health:', health);
        return health;
    } catch (error) {
        console.error('Health check failed:', error);
        return { status: 'unhealthy', error: error.message };
    }
}

// Export API helpers
window.HeartCheckAPI = {
    predictHeartRisk,
    checkAPIHealth
};

// Example usage (commented out):
/*
const examplePatient = {
    age: 57,
    sex: "male",
    resting_bp: 140,
    cholesterol: 240,
    fasting_bs_gt_120: 0,
    rest_ecg: "normal",
    max_hr: 150,
    exercise_angina: 0,
    oldpeak: 1.2,
    st_slope: "up",
    smoking: 0,
    diabetes: 0,
    family_history: 1
};

HeartCheckAPI.predictHeartRisk(examplePatient)
    .then(result => console.log('Prediction:', result))
    .catch(error => console.error('Error:', error));
*/

// ============================================
// ENHANCED STAT CARD ANIMATIONS
// ============================================

// Counter Animation for Stat Numbers
function animateCounter(element, target, duration = 2000) {
    const start = 0;
    const increment = target / (duration / 16);
    let current = start;
    
    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            current = target;
            clearInterval(timer);
        }
        
        // Format number with decimal for percentages
        if (target < 100) {
            element.textContent = current.toFixed(1);
        } else {
            element.textContent = Math.floor(current);
        }
    }, 16);
}

// Animate Progress Bars
function animateProgressBars() {
    const progressBars = document.querySelectorAll('.stat-bar-animated');
    
    progressBars.forEach(bar => {
        const targetWidth = bar.getAttribute('data-width');
        if (targetWidth) {
            bar.style.setProperty('--target-width', targetWidth + '%');
            setTimeout(() => {
                bar.style.width = targetWidth + '%';
            }, 100);
        }
    });
}

// Initialize Counters on Page Load
function initializeCounters() {
    const counters = document.querySelectorAll('.counter');
    
    // Use Intersection Observer for animation on scroll
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !entry.target.classList.contains('animated')) {
                entry.target.classList.add('animated');
                const target = parseFloat(entry.target.getAttribute('data-target'));
                animateCounter(entry.target, target);
            }
        });
    }, {
        threshold: 0.5
    });
    
    counters.forEach(counter => observer.observe(counter));
}

// Initialize on DOM Content Loaded
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        initializeCounters();
        animateProgressBars();
    });
} else {
    initializeCounters();
    animateProgressBars();
}
