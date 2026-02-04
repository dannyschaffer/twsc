<?php
/**
 * Template Name: Trader Check-In Tool
 */

get_header();
?>

<style>
    .checkin-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 4rem 1rem;
    }

    .checkin-header {
        text-align: center;
        margin-bottom: 4rem;
    }

    .checkin-header h1 {
        color: var(--navy);
        font-size: 3rem;
        margin-bottom: 1rem;
    }

    .checkin-header p {
        color: var(--text-secondary);
        font-size: 1.1rem;
        line-height: 1.6;
        max-width: 600px;
        margin: 0 auto;
    }

    .question-card {
        background: #fff;
        border: 1px solid rgba(0,0,0,0.08);
        border-radius: 12px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        transition: transform 0.3s ease;
    }
    
    .question-card:hover {
        transform: translateY(-2px);
    }

    .question-number {
        font-family: 'Space Mono', monospace;
        color: var(--gold);
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
        display: block;
        text-transform: uppercase;
    }

    .question-text {
        color: var(--navy);
        font-size: 1.2rem;
        font-weight: 500;
        margin-bottom: 2rem;
        font-family: 'Playfair Display', serif;
    }

    .scale-container {
        position: relative;
        padding: 0 1rem;
    }

    /* Track Line */
    .scale-track {
        position: absolute;
        top: 12px;
        left: 0;
        right: 0;
        height: 2px;
        background: #e0e0e0;
        z-index: 1;
    }

    .scale-options {
        display: flex;
        justify-content: space-between;
        position: relative;
        z-index: 2;
    }

    .scale-option {
        display: flex;
        flex-direction: column;
        align-items: center;
        cursor: pointer;
        width: 18%; /* Distribute width */
    }

    /* Radio Inputs (Hidden) */
    .scale-option input[type="radio"] {
        display: none;
    }

    /* Custom Checkbox/Dot */
    .scale-dot {
        width: 26px;
        height: 26px;
        background: #fff;
        border: 2px solid #ccc;
        border-radius: 50%; /* Make them squares like PDF? PDF has squares. Let's do rounded squares */
        border-radius: 4px; 
        margin-bottom: 10px;
        transition: all 0.2s ease;
        position: relative;
    }
    
    /* Center dot when selected */
    .scale-dot::after {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%) scale(0);
        width: 12px;
        height: 12px;
        background: var(--navy);
        border-radius: 2px;
        transition: transform 0.2s cubic-bezier(0.4, 0.0, 0.2, 1);
    }

    /* Selected State */
    .scale-option input[type="radio"]:checked + .scale-dot {
        border-color: var(--navy);
        box-shadow: 0 0 0 4px rgba(8, 51, 58, 0.1);
    }

    .scale-option input[type="radio"]:checked + .scale-dot::after {
        transform: translate(-50%, -50%) scale(1);
    }

    .scale-label {
        font-size: 0.8rem;
        color: var(--text-secondary);
        text-align: center;
        line-height: 1.2;
    }
    
    .scale-value {
        font-weight: 700;
        margin-bottom: 4px;
        color: var(--navy);
    }

    /* Result Section */
    .result-section {
        background: var(--navy);
        color: #fff;
        padding: 3rem;
        border-radius: 12px;
        text-align: center;
        margin-top: 4rem;
        display: none; /* Hidden by default */
        opacity: 0;
        transition: opacity 0.5s ease;
    }
    
    .result-section.visible {
        display: block;
        opacity: 1;
    }

    .score-display {
        font-size: 4rem;
        font-weight: 700;
        color: var(--gold);
        font-family: 'Space Mono', monospace;
        margin-bottom: 1rem;
    }

    .result-message {
        font-size: 1.5rem;
        font-family: 'Playfair Display', serif;
        margin-bottom: 2rem;
        line-height: 1.4;
    }
    
    .result-feedback {
        font-size: 1.1rem;
        opacity: 0.9;
        max-width: 600px;
        margin: 0 auto 2rem auto;
    }

    .btn-reset {
        background: transparent;
        border: 1px solid rgba(255,255,255,0.3);
        color: #fff;
        padding: 0.75rem 2rem;
        border-radius: 50px;
        cursor: pointer;
        font-family: 'Space Mono', monospace;
        text-transform: uppercase;
        margin-top: 1rem;
        transition: all 0.3s;
    }
    
    .btn-reset:hover {
        background: rgba(255,255,255,0.1);
        border-color: #fff;
    }

    @media (max-width: 600px) {
        .scale-label { font-size: 0.7rem; }
        .checkin-header h1 { font-size: 2rem; }
    }
</style>

<div class="checkin-container">
    <div class="checkin-header">
        <h1>Trader Check-In</h1>
        <p>Identify exactly where you are emotionally and psychologically before jumping into the market. Score yourself on a scale of 1 (Agree) to 5 (Disagree).</p>
    </div>

    <form id="checkInForm">
        <?php
        $questions = [
            1 => "You know how to look inward and identify what you might be feeling.",
            2 => "You are clear on what your values are.",
            3 => "Your experience of disappointment and/or frustration is minimal even when you lose.",
            4 => "You know when it's time to get up from your trading desk and take a break.",
            5 => "When you're not seeing your pattern, you're able to walk away and do something else.",
            6 => "You know after a big win you need to get back to neutrality.",
            7 => "You don't measure your self-worth against your profit and loss.",
            8 => "It doesn't take you long to bounce back from your mistakes.",
            9 => "You're true to your patterns no matter what.",
            10 => "You know that there is a trader who is just as confident of his/her position on the other side of any trade you make."
        ];

        foreach ($questions as $num => $q) : 
        ?>
        <div class="question-card" id="q<?php echo $num; ?>">
            <span class="question-number">Question <?php echo sprintf("%02d", $num); ?></span>
            <div class="question-text"><?php echo $q; ?></div>
            
            <div class="scale-container">
                <div class="scale-track"></div>
                <div class="scale-options">
                    <?php 
                    $labels = [
                        1 => "Agree",
                        2 => "Somewhat Agree",
                        3 => "Neutral",
                        4 => "Somewhat Disagree",
                        5 => "Disagree"
                    ];
                    foreach ($labels as $val => $text): ?>
                    <label class="scale-option">
                        <input type="radio" name="q<?php echo $num; ?>" value="<?php echo $val; ?>" onchange="calculateScore()">
                        <div class="scale-dot"></div>
                        <span class="scale-value"><?php echo $val; ?></span>
                        <span class="scale-label"><?php echo str_replace(' ', '<br>', $text); ?></span>
                    </label>
                    <?php endforeach; ?>
                </div>
            </div>
        </div>
        <?php endforeach; ?>
    </form>

    <div id="resultSection" class="result-section">
        <div style="text-transform: uppercase; font-family: 'Space Mono'; letter-spacing: 2px; margin-bottom: 1rem; opacity: 0.7;">Your Score</div>
        <div id="scoreDisplay" class="score-display">0</div>
        <div id="resultMessage" class="result-message"></div>
        <div id="resultFeedback" class="result-feedback"></div>
        
        <button class="btn-reset" onclick="resetForm()">Start Over</button>
        
        <div style="margin-top: 3rem; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 2rem;">
            <p style="font-size: 0.9rem; opacity: 0.7;">Ready to improve your score?</p>
            <a href="<?php echo site_url('/contact'); ?>" class="btn-primary" style="background: var(--gold); color: var(--navy); border: none;">Book a Consultation</a>
        </div>
    </div>
</div>

<script>
    function calculateScore() {
        // Collect all checked radios
        const form = document.getElementById('checkInForm');
        const formData = new FormData(form);
        let total = 0;
        let answeredParams = 0;

        for (let pair of formData.entries()) {
            total += parseInt(pair[1]);
            answeredParams++;
        }

        // Only show result if all 10 answered? Or show running total?
        // Let's show result once all are answered to prevent premature judgement
        if (answeredParams === 10) {
            showResult(total);
        }
    }

    function showResult(score) {
        const resultSection = document.getElementById('resultSection');
        const scoreDisplay = document.getElementById('scoreDisplay');
        const messageDisplay = document.getElementById('resultMessage');
        const feedbackDisplay = document.getElementById('resultFeedback');

        scoreDisplay.textContent = score;

        let message = "";
        let feedback = "";

        if (score <= 10) {
            message = "Wow!! Good job.";
            feedback = "Remember, there is more. Keep going.";
        } else if (score <= 19) {
            message = "You are so close to staying aware more.";
            feedback = "You know what is needed. Do that!";
        } else if (score <= 29) {
            message = "You are willing to be with 'what's hard to be with.'";
            feedback = "Well done! Go further.";
        } else if (score <= 39) {
            message = "You are closing your eyes to avoid some hard truths.";
            feedback = "With a little effort you will see change.";
        } else if (score <= 49) {
            message = "Your trading is harder than it should be.";
            feedback = "It is urgent you become more self aware.";
        } else {
            message = "You are emotionally asleep.";
            feedback = "Time to wake up!";
        }

        messageDisplay.textContent = message;
        feedbackDisplay.textContent = feedback;

        resultSection.classList.add('visible');
        
        // Smooth scroll to result
        resultSection.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

    function resetForm() {
        document.getElementById('checkInForm').reset();
        document.getElementById('resultSection').classList.remove('visible');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
</script>

<?php get_footer(); ?>
