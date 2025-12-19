// Podcast Episodes Data
const podcastEpisodes = [
    // 2025 Episodes
    {
        ep: 110,
        title: "Market Wizards Secrets Revealed with George Coyle",
        description: "Kim Ann Curtin sits down with co-author of the upcoming book Market Wizards: The Next Generation to discuss the philosophies, success, trading styles and more that the greatest traders across generations all have in common.",
        category: "wizards",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2025/11/110-Market-Wizard-Secrets-Revealed-wih-George-Coyle-1280-x-720-1024x576.jpg",
        link: "https://thewallstreetcoach.com/blog/2025/11/market-wizards-secrets-coyle/"
    },
    {
        ep: 109,
        title: "Why 99% of Profitable Traders Use a Journal with Edgewonk",
        description: "Kim Ann Curtin sits down with Edgewonk co-founders Rolf Schlotmann and Moritz Czubatinski to discuss the power of trading journals, the psychology of discipline, and the lessons learned from building the world's most comprehensive trading journal.",
        category: "mindset",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2025/10/109-Edgewonk-featured-1024x576.jpg",
        link: "https://thewallstreetcoach.com/blog/2025/10/ep-109-why-99-of-profitable-traders-use-a-journal-with-edgewonk/"
    },
    {
        ep: 108,
        title: "Mastering Risk and Self-Awareness with Gregg Sciabica",
        description: "Kim Ann Curtin sits down with Gregg Sciabica for a revealing conversation about emotional resilience, trading longevity, and the mindset required to navigate the ups and downs of professional trading.",
        category: "mindset",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2025/06/Gregg_Sciabica-TWSC-Youtube-Thumbnail-1024x576.jpg",
        link: "https://thewallstreetcoach.com/blog/2025/06/ep-108-mastering-risk-and-self-awareness-with-gregg-sciabica/"
    },
    {
        ep: 107,
        title: "Unshakeable: How Jeremy Aguiar Plays the Long Game in Day Trading",
        description: "Kim Ann Curtin sits down with trader Jeremy Aguiar, who brings 17 years of hard-won wisdom—from a major Chicago prop firm to trading solo. They dive into mindset, resilience, and why trading success is more about knowing yourself than the market.",
        category: "mindset",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2025/04/podcastnew-1280-x-720-px-1-1024x576.jpg",
        link: "https://thewallstreetcoach.com/blog/2025/04/ep-107-unshakeable-how-jeremy-aguiar-plays-the-long-game-in-day-trading/"
    },
    {
        ep: 106,
        title: "Mastering Risk with Neuroscience with Dr. Michael Platt",
        description: "Kim Ann Curtin welcomes renowned neuroscientist Dr. Michael Platt, Director of the Wharton Neuroscience Initiative and author of The Leader's Brain. Dr. Platt shares groundbreaking insights into how our brains make decisions—particularly under stress.",
        category: "neuro",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2025/03/Thumbnail-EP-106-Mastering-Risk-w-Neuroscience-w-Dr.-Michael-Platt-1-1-1024x576.jpg",
        link: "https://thewallstreetcoach.com/blog/2025/03/ep-106-mastering-risk-w-neuroscience-w-dr-michael-platt/"
    },
    {
        ep: 105,
        title: "The Mindset & Training of Top Traders with Jeff Holden of SMB Capital",
        description: "Jeff Holden, a trader and Head of Recruiting at SMB Capital, shares how mentorship, structured training, and a repeatable edge are key to long-term trading success.",
        category: "mindset",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2025/02/Copy-of-podcastimageNEW-1-1024x576.jpg",
        link: "https://thewallstreetcoach.com/blog/2025/02/the-mindset-training-of-top-traders-with-jeff-holden-of-smb-capital/"
    },
    {
        ep: 104,
        title: "From $2,000 to $1 Million – Matthew Monaco's Road to Trading Success",
        description: "Hear how trader Matthew Monaco turned a $2,000 investment and early failures into multimillion-dollar success!",
        category: "success",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2025/02/podcastimageNEW-1-1024x576.jpg",
        link: "https://thewallstreetcoach.com/blog/2025/02/ep-104-from-2000-to-1-million-matthew-monacos-road-to-trading-success/"
    },
    // 2024 Episodes
    {
        ep: 103,
        title: "Trader Moonshots with Bryce Tuohey",
        description: "Trader Bryce Tuohey dives into how he embraced risk and overcame internal doubts to pursue his passion for trading.",
        category: "mindset",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2024/12/podcastimageNEW-2-1024x576.jpg",
        link: "https://thewallstreetcoach.com/blog/2024/12/ep-103-trader-bryce-tuohey/"
    },
    {
        ep: 102,
        title: "Turning $2K into $1.6 MILLION with Eduardo Briceño",
        description: "Listen as Eduardo Briceño shares his journey of building a global trading community and achieving success by treating trading as a long-term career and business.",
        category: "success",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2024/11/The-Wall-Street-Coach-Podcast-Eduardo-Briceno-1024x576.jpg",
        link: "https://thewallstreetcoach.com/blog/2024/11/ep-102-turning-2k-into-1-6-million-with-eduardo-briceno/"
    },
    {
        ep: 101,
        title: "How To Biohack Your Trading",
        description: "Ian Ostrosky, Business Development Manager at Marek Health, joins us to discuss why traders need to focus on their health.",
        category: "neuro",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2024/10/The-Wall-Street-Coach-PodcastIan-Ostrosky-1024x576.jpg",
        link: "https://thewallstreetcoach.com/blog/2024/10/ep-101-how-to-biohack-your-trading/"
    },
    {
        ep: 100,
        title: "Teacher to Trading Mentor – Breaking Stereotypes with Danielle Shay",
        description: "Listen as Kim Ann Curtin sits down with trader, investor, market analyst, and expert commentator, Danielle Shay.",
        category: "success",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2024/10/Episode-100-Danielle-Shay-thumbnail-1024x576.jpg",
        link: "https://thewallstreetcoach.com/blog/2024/10/ep-100-teacher-to-trading-mentor-with-danielle-shay/"
    },
    {
        ep: 99,
        title: "One Good Trade with Mike Bellafiore",
        description: "Kim Ann Curtin sits down with Mike Bellafiore, co-founder of SMB Capital, one of the leading proprietary trading firms in the world and author of the trading classic books, One Good Trade and The Playbook.",
        category: "wizards",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2024/09/maxresdefault-1024x576.jpg",
        link: "https://thewallstreetcoach.com/blog/2024/09/ep-99-one-good-trade-with-mike-bellafiore/"
    },
    {
        ep: 98,
        title: "Trading Mastery: Uncovering Success with Pradeep Bonde",
        description: "Kim Ann Curtin sits down with veteran trader and Stockbee founder, Pradeep Bonde, to dive deep into the art of mastering the markets.",
        category: "wizards",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2024/09/Thumbnail_1-1-1024x576.jpg",
        link: "https://thewallstreetcoach.com/blog/2024/09/ep-98-trading-mastery-uncovering-success-with-pradeep-bonde/"
    },
    {
        ep: 97,
        title: "Why Most Traders Fail at Risk Management",
        description: "Kim welcomes back Brian Lee to discuss the often misunderstood concept of risk in trading, emphasizing its importance for both novice and experienced traders.",
        category: "mindset",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2024/06/EP-97-1024x576.jpg",
        link: "https://thewallstreetcoach.com/blog/2024/06/ep-97-why-most-traders-fail-at-risk-management/"
    },
    {
        ep: 96,
        title: "Choosing the Best Broker for Active Traders and Retail Trading",
        description: "Matt Marino, Co-Founder of CenterPoint chats about shorting low float stocks, building client relationships, managing stress, and advanced trading tools.",
        category: "strategy",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2024/05/thumbnail-ep-96-1024x576.jpg",
        link: "https://thewallstreetcoach.com/blog/2024/05/matt-marino-co-founder-of-centerpoint/"
    },
    {
        ep: 95,
        title: "Trading Made Simple – Cutting Through the Noise with Chris Lanzilotti",
        description: "Guest Chris Lanzilotti demystifies the complexities of trading, offering clear, actionable strategies for traders of all levels.",
        category: "strategy",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2024/05/trade-simple-1024x576.jpg",
        link: "https://thewallstreetcoach.com/blog/2024/05/the-wall-street-coach-chris-lanzilotti/"
    },
    {
        ep: 94,
        title: "Bouncing Back from Trading Losses – Lessons from Matt 'PAX' Kenah",
        description: "Matt 'PAX' Kenah shares his insightful journey on bouncing back from significant trading losses to building a resilient trading strategy.",
        category: "mindset",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2024/05/File-822x1024.jpg",
        link: "https://thewallstreetcoach.com/blog/2024/05/trader-matt-pax-kenah/"
    },
    {
        ep: 93,
        title: "From IT Professional to Successful Trader",
        description: "Stan Ivanov shares his unique journey from growing up in Bulgaria to becoming a successful trader in Las Vegas, highlighting how his IT background shaped his trading strategy.",
        category: "success",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2024/04/EP-93-1024x585.jpg",
        link: "https://thewallstreetcoach.com/blog/2024/04/ep-93-from-it-professional-to-successful-trader/"
    },
    {
        ep: 92,
        title: "Embracing the Unpredictable – The Day Trader's Guide to Uncertainty",
        description: "Explore the profound impact of embracing uncertainty as a catalyst for growth, creativity, and resilience within the volatile world of day trading with Maggie Jackson.",
        category: "mindset",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2024/03/EP92-podcast-1024x576.jpg",
        link: "https://thewallstreetcoach.com/blog/2024/03/maggie-jackson-uncertainty/"
    },
    {
        ep: 91,
        title: "Angry After Trading? Discover This Quick Anger-Release Trick",
        description: "Discover how transforming anger through a unique expression method can pave the way for personal growth and improved mental well-being.",
        category: "mindset",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2024/03/ep-91-1024x576.jpg",
        link: "https://thewallstreetcoach.com/blog/2024/03/dave-shoemaker-tattoo/"
    },
    {
        ep: 90,
        title: "Don't Let Your Mind Sabotage Your Trading: Master the Mental Game with Steven Goldstein",
        description: "Steven Goldstein explores the transformative journey of becoming a consistently successful trader, shedding light on the often-overlooked elements of vulnerability and purpose.",
        category: "mindset",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2024/02/ep90-wsc-1024x576.jpg",
        link: "https://thewallstreetcoach.com/blog/2024/02/ep-90-dont-let-your-mind-sabotage-your-trading-master-the-mental-game-of-trading-with-steven-goldstein/"
    },
    {
        ep: 89,
        title: "Big Waves to Big Trades – Building a Trading Tribe in the Surf Community",
        description: "Explore the unique intersection of surfing and stock trading with Shane Dorian and Ryan Miller who've mastered both.",
        category: "success",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2024/02/trading-tibe-ep-89-1024x576.jpg",
        link: "https://thewallstreetcoach.com/blog/2024/02/shane-dorian-and-ryan-miller/"
    },
    {
        ep: 88,
        title: "Reminiscences of a Day Trader with David S. Hale",
        description: "David Hale talks about the harsh realities of day trading and what traders can expect if they choose to pursue a career in day trading.",
        category: "mindset",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2024/01/ep-88-1024x576.jpeg",
        link: "https://thewallstreetcoach.com/blog/2024/01/ep-88-reminiscences-of-a-day-trader-with-david-s-hale/"
    },
    {
        ep: 87,
        title: "No Worries – How to Live a Stress-Free Financial Life with Jared Dillian",
        description: "Jared Dillian, author of 'No Worries: How to Live a Stress-Free Financial Life,' discusses cultivating a healthy relationship with money to eliminate financial stress.",
        category: "mindset",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2024/01/Jared-D-Podcast-1024x576.jpg",
        link: "https://thewallstreetcoach.com/blog/2024/01/jared-dillian/"
    },
    {
        ep: 86,
        title: "How This Trader Turned 'Boring' into Seven Figures (while in college)!",
        description: "Kyle Williams managed to reach seven figures by staying true to his process rather than succumbing to short-term excitement.",
        category: "success",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2024/01/student-to-7-figure-podcast-1024x576.jpg",
        link: "https://thewallstreetcoach.com/blog/2024/01/kyle-williams/"
    },
    // 2023 Episodes
    {
        ep: 85,
        title: "Gratitude is the Attitude with Ricky Analog",
        description: "Ricky Analog, a seasoned trader with more than a decade of trading under his belt, talks about how gratitude is a game-changer, not just in trading, but in your everyday life.",
        category: "mindset",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2023/10/Ricky-Analog-1024x576.jpg",
        link: "https://thewallstreetcoach.com/blog/2023/10/ricky-analog-gratitude/"
    },
    {
        ep: 84,
        title: "Sam Prior on Trading, Sports & Mindset",
        description: "Sam Prior, a semi-pro rugby player turned successful day trader, dives into his journey from a career in orthopedic account management to trading.",
        category: "mindset",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2023/10/SamPrior-1024x576.jpg",
        link: "https://thewallstreetcoach.com/blog/2023/10/sam-prior/"
    },
    {
        ep: 83,
        title: "Peter Atwater on Confidence-Driven Decision-Making",
        description: "Author Peter Atwater discusses his book, 'The Confidence Map,' which is a current must-read for anyone who wants to improve their decision-making.",
        category: "mindset",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2023/08/Peter-Atwater-1-1024x576.jpg",
        link: "https://thewallstreetcoach.com/blog/2023/08/ep-83-peter-atwater-on-confidence-driven-decision-making/"
    },
    {
        ep: 82,
        title: "Seeking Alpha's Steven Cress on the Importance of Data-driven Trading & Investing",
        description: "Steven Cress, the head of quantitative strategies at Seeking Alpha, shares his journey and insights into how Seeking Alpha's platform is changing the landscape of investment research.",
        category: "strategy",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2023/08/Steven-Cress-Rectangle-1024x576.jpg",
        link: "https://thewallstreetcoach.com/blog/2023/08/steven-cress/"
    },
    {
        ep: 81,
        title: "Trading Solutions with Mondeum Capital's Mike Milani",
        description: "Mike Milani, CEO of Mondeum Capital and a seasoned professional with 25 years of experience in active trading and financial technology, discusses what it takes to be a successful trader.",
        category: "strategy",
        image: "https://thewallstreetcoach.com/wp-content/uploads/2023/07/Mike-Milani-1-1024x576.jpg",
        link: "https://thewallstreetcoach.com/blog/2023/07/ep-81-trading-solutions-with-mondeum-capitals-mike-milani/"
    }
];

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = podcastEpisodes;
}
