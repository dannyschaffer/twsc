<?php
/**
 * Template Name: TPI Assessment Page
 */

get_header();
?>

<style>
    .tpi-diamond-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 4rem;
        align-items: center;
        max-width: 1000px;
        margin: 3rem auto;
    }

    .roi-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 2rem;
        max-width: 900px;
        margin: 3rem auto;
        align-items: start;
    }

    @media (max-width: 768px) {
        .tpi-diamond-container {
            grid-template-columns: 1fr !important;
            gap: 2rem !important;
        }

        .roi-grid {
            grid-template-columns: 1fr !important;
        }
    }
</style>

<!-- Hero Section: Results Hook -->
<section class="hero hero-tpi">
    <div class="hero-overlay"></div>
    <div class="container">
        <div class="hero-content" style="text-align: center;">
            <h1 class="hero-headline">Are You Ready to Trade Without Fear?</h1>
            <p class="hero-subheadline">Answer 15 questions to find out why you're hesitating and exactly what to do
                about it.</p>
            <a href="<?php echo site_url('/book'); ?>" class="btn-cta">Book a Discovery Call</a>
        </div>
    </div>
</section>

<!-- Who Is This For? Section -->
<section class="section" style="background-color: #08333A; color: white;">
    <div class="container">
        <h2 style="text-align: center; color: white;">Who Is The Trader Positioning Index For?</h2>
        <p class="section-intro" style="color: rgba(255, 255, 255, 0.9);">Designed for serious market participants
            who know that "90% of trading is mental."
        </p>

        <div class="steps-grid" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
            <div class="step-card" style="border: 1px solid rgba(255,255,255,0.2); background: rgba(255,255,255,0.05);">
                <h3 style="color: var(--gold);">Independent Retail Traders</h3>
                <p style="color: rgba(255, 255, 255, 0.8);">You have the strategy, but you're stuck in a "boom and
                    bust" cycle. You battle FOMO, revenge trading, and hesitation. <strong
                        style="color: #fff;">Goal:</strong> Consistent
                    profitability and emotional stability.</p>
            </div>
            <div class="step-card" style="border: 1px solid rgba(255,255,255,0.2); background: rgba(255,255,255,0.05);">
                <h3 style="color: var(--gold);">Portfolio Managers & Prop Traders</h3>
                <p style="color: rgba(255, 255, 255, 0.8);">You operate in high-stakes environments. You need to
                    protect your longevity and execute without hesitation. <strong style="color: #fff;">Goal:</strong>
                    Peak performance,
                    higher Sharpe ratio, and avoiding burnout.</p>
            </div>
            <div class="step-card" style="border: 1px solid rgba(255,255,255,0.2); background: rgba(255,255,255,0.05);">
                <h3 style="color: var(--gold);">High-Performing Executives</h3>
                <p style="color: rgba(255, 255, 255, 0.8);">You're a success in business, but the market humbles
                    you.
                    Your usual "force of will" doesn't work here. <strong style="color: #fff;">Goal:</strong> Align
                    your high-performance
                    identity with market realities.</p>
            </div>
        </div>
    </div>
</section>

<!-- Value Proposition: Measure & Improve -->
<section class="section">
    <div class="container">
        <h2 style="text-align: center;">We Measure & Improve 3 Key Areas</h2>
        <p class="section-intro">Stop guessing why you're losing. We use clinical data to optimize your:</p>

        <div class="steps-grid">
            <div class="step-card">
                <div class="step-number">1</div>
                <h3>Risk Tolerance</h3>
                <p>Are you wired to freeze or fight? We measure your instinctive response to volatility.
                </p>
            </div>
            <div class="step-card">
                <div class="step-number">2</div>
                <h3>Emotional Regulation</h3>
                <p>How quickly do you recover from a loss? We quantify your "Tilt Threshold" and recovery speed.</p>
            </div>
            <div class="step-card">
                <div class="step-number">3</div>
                <h3>Cognitive Flexibility</h3>
                <p>Can you flip your bias when the market changes? We test your neuroplasticity under pressure.</p>
            </div>
        </div>
    </div>
</section>

<!-- Credibility: Research & Stats -->
<section class="section section-dark">
    <div class="container">
        <h2 style="text-align: center;">Backed by Years of Wall Street Data</h2>
        <p class="section-intro">The Trader Positioning Index (TPI) is a clinical-grade judgment assessment that
            measures
            70+ indicators of a trader's decision-making capacity under pressure. It is not a personality
            quiz—it’s an instrument built on the profiles of elite leaders and nominated for a Nobel Prize.</p>

        <div class="tpi-diamond-container">
            <!-- Left Column: Text & Bullets -->
            <div class="tpi-content-side" style="display: flex; flex-direction: column; gap: 2rem;">
                <div>
                    <h3 style="color: var(--gold); margin-bottom: 1rem;">The "Blue Diamond" Diagnostic</h3>
                    <p style="margin-bottom: 0; color: var(--text-secondary);">Your TPI report visualizes your
                        judgment in a coherent shape. A balanced, expanded diamond represents a mind optimized for
                        probability. A collapsed or skewed diamond reveals exactly where your judgment is breaking
                        down under stress.</p>
                </div>

                <div class="tpi-bullets-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                    <div class="dimension-item">
                        <div class="dimension-dot"></div>
                        <span>Risk Tolerance</span>
                    </div>
                    <div class="dimension-item">
                        <div class="dimension-dot"></div>
                        <span>Emotional Regulation</span>
                    </div>
                    <div class="dimension-item">
                        <div class="dimension-dot"></div>
                        <span>Decision Speed</span>
                    </div>
                    <div class="dimension-item">
                        <div class="dimension-dot"></div>
                        <span>Loss Recovery</span>
                    </div>
                    <div class="dimension-item">
                        <div class="dimension-dot"></div>
                        <span>Cognitive Flexibility</span>
                    </div>
                    <div class="dimension-item">
                        <div class="dimension-dot"></div>
                        <span>Process Adherence</span>
                    </div>
                </div>
            </div>

            <!-- Right Column: Image -->
            <div class="tpi-diamond" style="max-width: 100%;">
                <svg viewBox="0 0 400 400" width="100%" height="100%">
                    <!-- Radar chart background -->
                    <defs>
                        <radialGradient id="radarGradient">
                            <stop offset="0%" style="stop-color:#E9B34C;stop-opacity:0.3" />
                            <stop offset="100%" style="stop-color:#E9B34C;stop-opacity:0" />
                        </radialGradient>
                    </defs>

                    <!-- Grid circles -->
                    <circle cx="200" cy="200" r="150" fill="none" stroke="#E9B34C" stroke-width="1" opacity="0.2" />
                    <circle cx="200" cy="200" r="120" fill="none" stroke="#E9B34C" stroke-width="1" opacity="0.2" />
                    <circle cx="200" cy="200" r="90" fill="none" stroke="#E9B34C" stroke-width="1" opacity="0.2" />
                    <circle cx="200" cy="200" r="60" fill="none" stroke="#E9B34C" stroke-width="1" opacity="0.2" />
                    <circle cx="200" cy="200" r="30" fill="none" stroke="#E9B34C" stroke-width="1" opacity="0.2" />

                    <!-- Axis lines -->
                    <line x1="200" y1="200" x2="200" y2="50" stroke="#E9B34C" stroke-width="2" opacity="0.5" />
                    <line x1="200" y1="200" x2="342.5" y2="292.5" stroke="#E9B34C" stroke-width="2" opacity="0.5" />
                    <line x1="200" y1="200" x2="107.5" y2="292.5" stroke="#E9B34C" stroke-width="2" opacity="0.5" />
                    <line x1="200" y1="200" x2="57.5" y2="107.5" stroke="#E9B34C" stroke-width="2" opacity="0.5" />
                    <line x1="200" y1="200" x2="342.5" y2="107.5" stroke="#E9B34C" stroke-width="2" opacity="0.5" />

                    <!-- Sample data polygon -->
                    <polygon points="200,80 280,220 170,280 120,180 260,140" fill="url(#radarGradient)" stroke="#E9B34C"
                        stroke-width="2" />
                </svg>
            </div>
        </div>
    </div>
</section>

<!-- Process: How It Works -->
<section class="section">
    <div class="container">
        <h2 style="text-align: center;">How It Works</h2>
        <p class="section-intro">From Diagnosis to Edge in 3 Simple Steps.</p>

        <div class="steps-grid">
            <div class="step-card">
                <div class="step-number">1</div>
                <h3>The Assessment</h3>
                <p><strong>15 Minutes Online.</strong> Unlike personality tests that ask generic questions, this
                    measures how you prioritize values. It bypasses conscious bias to reveal your true
                    decision-making framework.</p>
            </div>
            <div class="step-card">
                <div class="step-number">2</div>
                <h3>The Analysis</h3>
                <p><strong>The "Blue Diamond" Report.</strong> You receive a 35+ page personalized narrative. It
                    includes the "Diamond Index" visualization - an X-ray of your judgment across 70+ indicators,
                    not
                    just a text summary.</p>
            </div>
            <div class="step-card">
                <div class="step-number">3</div>
                <h3>The Debrief</h3>
                <p><strong>The Breakthrough.</strong> A 60-minute strategy session to turn insight into action. We
                    don't just diagnose; we prescribe. You'll leave with a plan to "trade around" your blind spots.
                </p>
            </div>
        </div>
    </div>
</section>

<!-- Pain vs Gain Section -->
<section class="section section-dark">
    <div class="container">
        <h2 style="text-align: center;">The ROI of Self-Mastery</h2>

        <div class="roi-grid">
            <div
                style="padding: 2rem; background: rgba(255,100,100,0.05); border-radius: 12px; border: 1px solid rgba(255,100,100,0.1);">
                <h3 style="color: #ff6b6b; margin-bottom: 1.5rem;">The Cost of Blind Spots</h3>
                <ul class="check-list" style="list-style: none; margin: 0;">
                    <li style="margin-bottom: 1rem; display: flex; align-items: flex-start; gap: 0.75rem;">
                        <span style="color: #ff6b6b;">✕</span> Inconsistent P&L curves
                    </li>
                    <li style="margin-bottom: 1rem; display: flex; align-items: flex-start; gap: 0.75rem;">
                        <span style="color: #ff6b6b;">✕</span> "Revenge trading" after losses
                    </li>
                    <li style="margin-bottom: 1rem; display: flex; align-items: flex-start; gap: 0.75rem;">
                        <span style="color: #ff6b6b;">✕</span> Hesitation on good setups
                    </li>
                    <li style="margin-bottom: 1rem; display: flex; align-items: flex-start; gap: 0.75rem;">
                        <span style="color: #ff6b6b;">✕</span> High stress & burnout
                    </li>
                </ul>
            </div>

            <div
                style="padding: 2rem; background: rgba(16, 185, 129, 0.05); border-radius: 12px; border: 1px solid rgba(16, 185, 129, 0.1);">
                <h3 style="color: var(--teal); margin-bottom: 1.5rem;">The Trader Positioning Index Edge</h3>
                <ul class="check-list" style="list-style: none; margin: 0;">
                    <li style="margin-bottom: 1rem; display: flex; align-items: flex-start; gap: 0.75rem;">
                        <span style="color: var(--teal);">✓</span> clarity on "Self-Sabotage" triggers
                    </li>
                    <li style="margin-bottom: 1rem; display: flex; align-items: flex-start; gap: 0.75rem;">
                        <span style="color: var(--teal);">✓</span> Higher Sharpe ratio & consistency
                    </li>
                    <li style="margin-bottom: 1rem; display: flex; align-items: flex-start; gap: 0.75rem;">
                        <span style="color: var(--teal);">✓</span> "Peace of mind" in execution
                    </li>
                    <li style="margin-bottom: 1rem; display: flex; align-items: flex-start; gap: 0.75rem;">
                        <span style="color: var(--teal);">✓</span> Longevity in your trading career
                    </li>
                </ul>
            </div>
        </div>
    </div>
</section>

<!-- Pricing Section: CTA -->
<section class="section" id="pricing">
    <div class="container">
        <h2 style="text-align: center;">Get Your Score</h2>

        <div class="pricing-cards">
            <!-- TPI CARD -->
            <div class="pricing-card">
                <h3>Trader Positioning Index</h3>
                <div class="price">$1,295</div>
                <ul class="pricing-features">
                    <li>15-Minute Online Assessment</li>
                    <li>Comprehensive "Trader Avatar" Report</li>
                    <li>Comparison to Elite Fund Manager Benchmarks</li>
                    <li>Custom Action Roadmap</li>
                    <li>One-on-One Coaching Review</li>
                </ul>
                <a href="<?php echo site_url('/book'); ?>" class="btn-secondary">Book a Consultation</a>
            </div>

            <!-- EPI CARD -->
            <div class="pricing-card">
                <h3>Executive Positioning Index</h3>
                <div class="price">$1,595</div>
                <ul class="pricing-features">
                    <li>"X-Ray" of Your Strengths & Blind Spots</li>
                    <li>Measures 70+ Areas of Judgment</li>
                    <li>35+ Page Personalized Blueprint</li>
                    <li>60-Min One-on-One Coaching Session</li>
                    <li>Follow-up Coaching Check-In (1 Month)</li>
                </ul>
                <a href="<?php echo site_url('/book'); ?>" class="btn-cta">Book a Consultation</a>
            </div>
        </div>
    </div>
</section>

<!-- Testimonials -->
<section class="section section-dark">
    <div class="container">
        <h2 style="text-align: center;">What Traders Are Saying</h2>

        <div class="testimonials-grid">
            <div class="testimonial-card">
                <blockquote>"The TPI revealed blind spots I didn't even know I had. My win rate increased 23% in the
                    first month."</blockquote>
                <cite>- Portfolio Manager, Hedge Fund</cite>
            </div>
            <div class="testimonial-card">
                <blockquote>"Finally, a data-driven approach to trading psychology. This isn't fluff - it's
                    actionable
                    science."</blockquote>
                <cite>- Independent Trader</cite>
            </div>
            <div class="testimonial-card">
                <blockquote>"The assessment pinpointed exactly why I was giving back profits. Game-changing."
                </blockquote>
                <cite>- Prop Trader</cite>
            </div>
        </div>
    </div>
</section>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Trader Positioning Index",
  "image": "https://thewallstreetcoach.com/wp-content/themes/twsc-theme/assets/images/The-Wall-Street-Coach-Logo-Transparent@white.png",
  "description": "A clinical-grade judgment assessment that measures 70+ indicators of a trader's decision-making capacity under pressure.",
  "brand": {
    "@type": "Brand",
    "name": "The Wall Street Coach"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://thewallstreetcoach.com/assessment",
    "priceCurrency": "USD",
    "price": "1295.00",
    "availability": "https://schema.org/InStock"
  }
}
</script>

<?php get_footer(); ?>