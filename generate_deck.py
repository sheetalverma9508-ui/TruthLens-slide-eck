"""
TruthLens - Hackathon PowerPoint Deck Generator
Generates a 12-slide modern dark-tech presentation.
Requirements: pip install python-pptx
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck(filename="TruthLens_Hackathon_Presentation.pptx"):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Color Palette: Modern Navy, Blue, and Cyan
    BG_NAVY = RGBColor(10, 17, 40)        # #0A1128
    CARD_BG = RGBColor(0, 31, 84)         # #001F54
    CYAN_ACCENT = RGBColor(0, 229, 255)   # #00E5FF
    TEXT_WHITE = RGBColor(255, 255, 255)  # #FFFFFF
    TEXT_MUTED = RGBColor(170, 185, 210)  # Soft silver-blue

    blank_layout = prs.slide_layouts[6]

    def set_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_NAVY
        bg.line.fill.background()
        return bg

    def add_header(slide, title, subtitle):
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.7), Inches(1.2))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = title.upper()
        p.font.size = Pt(26)
        p.font.bold = True
        p.font.color.rgb = CYAN_ACCENT

        p2 = tf.add_paragraph()
        p2.text = subtitle
        p2.font.size = Pt(14)
        p2.font.color.rgb = TEXT_MUTED

    def add_card(slide, left, top, width, height, title, body_bullets):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = CYAN_ACCENT
        card.line.width = Pt(1.2)

        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.25)
        tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.25)

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = CYAN_ACCENT

        for bullet in body_bullets:
            p_b = tf.add_paragraph()
            p_b.text = "• " + bullet
            p_b.font.size = Pt(13)
            p_b.font.color.rgb = TEXT_WHITE
            p_b.space_before = Pt(6)

    # ---------------- SLIDE 1: TITLE SLIDE ----------------
    s1 = prs.slides.add_slide(blank_layout)
    set_background(s1)
    
    t_box = s1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.3), Inches(3.0))
    tf1 = t_box.text_frame
    tf1.word_wrap = True
    
    p = tf1.paragraphs[0]
    p.text = "TRUTHLENS"
    p.font.size = Pt(56)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p.alignment = PP_ALIGN.CENTER
    
    p2 = tf1.add_paragraph()
    p2.text = "AI-Powered Fake News Detection System"
    p2.font.size = Pt(24)
    p2.font.color.rgb = TEXT_WHITE
    p2.alignment = PP_ALIGN.CENTER

    p3 = tf1.add_paragraph()
    p3.text = "Detecting Misinformation Through Explainable Artificial Intelligence"
    p3.font.size = Pt(16)
    p3.font.color.rgb = TEXT_MUTED
    p3.alignment = PP_ALIGN.CENTER

    add_card(s1, Inches(2.2), Inches(4.8), Inches(4.2), Inches(1.8), "Team Identity", 
             ["Team: [Your Team Name]", "Hackathon: National AI Finals 2026", "Domain: AI for Social Impact"])
    add_card(s1, Inches(6.9), Inches(4.8), Inches(4.2), Inches(1.8), "Key Technologies", 
             ["Python & Scikit-Learn", "Natural Language Processing (NLP)", "Streamlit Reactive UI"])

    # ---------------- SLIDE 2: THE REAL-WORLD PROBLEM ----------------
    s2 = prs.slides.add_slide(blank_layout)
    set_background(s2)
    add_header(s2, "The Real-World Problem", "The Infodemic: How Unchecked Misinformation Impacts Modern Society")
    
    w4 = Inches(2.7)
    add_card(s2, Inches(0.8), Inches(2.0), w4, Inches(4.4), "Viral Velocity", 
             ["Spreads 6x faster than truth", "Exploits high-arousal emotions", "Forwarded endlessly without friction"])
    add_card(s2, Inches(3.8), Inches(2.0), w4, Inches(4.4), "Zero Verification", 
             ["No built-in check in chat apps", "Instant 1-click shares", "Echo chambers amplify falsehoods"])
    add_card(s2, Inches(6.8), Inches(2.0), w4, Inches(4.4), "Public Confusion", 
             ["Healthcare panic & rumors", "Financial & stock manipulation", "Erosion of trust in legitimate news"])
    add_card(s2, Inches(9.8), Inches(2.0), w4, Inches(4.4), "Real-World Harm", 
             ["Misguided civic decisions", "Communal & social polarization", "Permanent reputational damage"])

    # ---------------- SLIDE 3: PROBLEM STATEMENT ----------------
    s3 = prs.slides.add_slide(blank_layout)
    set_background(s3)
    add_header(s3, "The Problem Statement", "The Critical Gap in Current Misinformation Countermeasures")
    
    add_card(s3, Inches(1.0), Inches(2.2), Inches(5.3), Inches(4.2), "Limitations of Manual Fact-Checking",
             ["High Latency: Takes hours to days to verify claims",
              "Unscalable: Cannot keep pace with millions of daily posts",
              "Inaccessible: Not available at the immediate point-of-read",
              "Reactive: Debunking arrives long after viral spread"])
    
    add_card(s3, Inches(7.0), Inches(2.2), Inches(5.3), Inches(4.2), "The Need for TruthLens",
             ["Automated First-Line Screening: Sub-second analysis",
              "Explainability: Unpacks WHY text appears suspicious",
              "Uncertainty Awareness: Honest about borderline cases",
              "Democratized Access: Free, simple, browser-accessible"])

    # ---------------- SLIDE 4: PROPOSED SOLUTION ----------------
    s4 = prs.slides.add_slide(blank_layout)
    set_background(s4)
    add_header(s4, "The Proposed Solution", "TruthLens: Intelligent, Transparent News Credibility Screening")
    
    w2 = Inches(5.6)
    add_card(s4, Inches(0.8), Inches(2.0), w2, Inches(2.3), "1. Tri-State Classification",
             ["Classifies into REAL, FAKE, or UNCERTAIN", "Avoids binary forced guessing on ambiguous text"])
    add_card(s4, Inches(6.9), Inches(2.0), w2, Inches(2.3), "2. Calibrated Confidence Score",
             ["Provides honest probability metrics (e.g. 89% vs 52%)", "Allows users to gauge certainty levels"])
    add_card(s4, Inches(0.8), Inches(4.6), w2, Inches(2.3), "3. Explainable AI (XAI)",
             ["Highlights influential words driving model outputs", "Educates users on clickbait & sensationalism cues"])
    add_card(s4, Inches(6.9), Inches(4.6), w2, Inches(2.3), "4. Ethical AI Safeguards",
             ["Clear disclaimers: AI screening is not definitive truth", "Encourages verification with official news wires"])

    # ---------------- SLIDE 5: HOW IT WORKS ----------------
    s5 = prs.slides.add_slide(blank_layout)
    set_background(s5)
    add_header(s5, "How It Works", "The End-to-End NLP & Inference Workflow in Under 150ms")
    
    steps = [
        ("Step 1: Input", ["Paste headline or article body text"]),
        ("Step 2: Preprocess", ["Regex cleaning, tokenizing, stopword removal"]),
        ("Step 3: Vectorize", ["TF-IDF n-gram feature mapping"]),
        ("Step 4: Predict", ["Linear probability computation"]),
        ("Step 5: Explain", ["Extract top coefficient tokens & render UI"])
    ]
    for i, (stitle, sbullets) in enumerate(steps):
        add_card(s5, Inches(0.8 + i * 2.4), Inches(2.4), Inches(2.2), Inches(4.0), stitle, sbullets)

    # ---------------- SLIDE 6: TECH STACK ----------------
    s6 = prs.slides.add_slide(blank_layout)
    set_background(s6)
    add_header(s6, "Technology Stack", "Engineered for High Throughput, Zero GPU Overhead, and Interpretability")
    
    add_card(s6, Inches(0.8), Inches(2.2), Inches(3.6), Inches(2.2), "Python 3.10+",
             ["Core programming language", "Vast ecosystem for NLP & ML"])
    add_card(s6, Inches(4.8), Inches(2.2), Inches(3.6), Inches(2.2), "Pandas & NumPy",
             ["High-performance data handling", "Matrix and vectorized math"])
    add_card(s6, Inches(8.8), Inches(2.2), Inches(3.6), Inches(2.2), "Scikit-Learn",
             ["Logistic Regression & Naive Bayes", "Pipelines and evaluation metrics"])
    add_card(s6, Inches(0.8), Inches(4.7), Inches(3.6), Inches(2.2), "TF-IDF Vectorizer",
             ["Captures unigram and bigram patterns", "Penalizes frequent non-informative words"])
    add_card(s6, Inches(4.8), Inches(4.7), Inches(3.6), Inches(2.2), "Streamlit",
             ["Modern reactive web UI", "Interactive gauges and token highlighters"])
    add_card(s6, Inches(8.8), Inches(4.7), Inches(3.6), Inches(2.2), "Matplotlib & Seaborn",
             ["Confusion matrix visualizers", "ROC and Precision-Recall analytics"])

    # ---------------- SLIDE 7: ARCHITECTURE ----------------
    s7 = prs.slides.add_slide(blank_layout)
    set_background(s7)
    add_header(s7, "System Architecture", "Modular Multi-Tier Software & Inference Design")
    
    w3 = Inches(3.6)
    add_card(s7, Inches(0.8), Inches(2.2), w3, Inches(4.5), "Client / UI Tier",
             ["Streamlit Application", "Text area for article input", "Dynamic confidence gauge", "Highlighted keyword viewer", "Safety disclaimer banner"])
    add_card(s7, Inches(4.8), Inches(2.2), w3, Inches(4.5), "Processing Tier",
             ["Text Normalizer & Cleaner", "Regex noise scrubber", "TF-IDF Vectorizer Transformer", "Uncertainty Boundary Filter", "Feature Importance Extractor"])
    add_card(s7, Inches(8.8), Inches(2.2), w3, Inches(4.5), "Model & Data Tier",
             ["Pre-trained ML Model Weights", "Pre-fitted TF-IDF Vocabulary", "Serialized .joblib artifacts", "Leakage-free training pipelines"])

    # ---------------- SLIDE 8: INNOVATION ----------------
    s8 = prs.slides.add_slide(blank_layout)
    set_background(s8)
    add_header(s8, "Innovation & Unique Features", "What Sets TruthLens Apart from Generic Classifiers")
    
    add_card(s8, Inches(0.8), Inches(2.0), w2, Inches(2.3), "Explainable AI (XAI)",
             ["Transparent keyword influence scores", "Demystifies why content was flagged"])
    add_card(s8, Inches(6.9), Inches(2.0), w2, Inches(2.3), "Uncertainty Handling",
             ["Labels 45-55% predictions as UNCERTAIN", "Prevents hallucinated or forced accuracy"])
    add_card(s8, Inches(0.8), Inches(4.6), w2, Inches(2.3), "Ultra-Lightweight Inference",
             ["Runs on CPU in under 150ms", "Zero expensive GPU dependencies"])
    add_card(s8, Inches(6.9), Inches(4.6), w2, Inches(2.3), "Data Leakage Prevention",
             ["Strict train/test isolated vectorization", "Honest, reliable evaluation metrics"])

    # ---------------- SLIDE 9: IMPACT ----------------
    s9 = prs.slides.add_slide(blank_layout)
    set_background(s9)
    add_header(s9, "Practical Application & Impact", "Empowering Everyday Digital Citizens and Information Professionals")
    
    add_card(s9, Inches(0.8), Inches(2.0), w2, Inches(2.3), "Everyday Social Media Users",
             ["5-second check before forwarding messages", "Reduces spread of viral WhatsApp rumors"])
    add_card(s9, Inches(6.9), Inches(2.0), w2, Inches(2.3), "Journalists & Newsrooms",
             ["Automated initial screening for tip lines", "Triage thousands of user submissions"])
    add_card(s9, Inches(0.8), Inches(4.6), w2, Inches(2.3), "Students & Educators",
             ["Digital literacy training tool", "Teaches critical analysis of online content"])
    add_card(s9, Inches(6.9), Inches(4.6), w2, Inches(2.3), "Societal & Civic Health",
             ["Deters election & healthcare falsehoods", "Fosters an evidence-first culture"])

    # ---------------- SLIDE 10: ROADMAP ----------------
    s10 = prs.slides.add_slide(blank_layout)
    set_background(s10)
    add_header(s10, "Feasibility & Implementation", "Our 6-Phase Engineering Lifecycle")
    
    stages = [
        ("Phase 1: Dataset", ["Balanced real/fake corpora collection"]),
        ("Phase 2: Cleaning", ["Leakage-free text preprocessing"]),
        ("Phase 3: TF-IDF", ["N-gram feature extraction"]),
        ("Phase 4: ML Models", ["Logistic Regression & Naive Bayes"]),
        ("Phase 5: App Dev", ["Streamlit UI & explainability engine"]),
        ("Phase 6: Validation", ["Stress-test against unseen contemporary news"])
    ]
    for i, (title, b) in enumerate(stages):
        add_card(s10, Inches(0.8 + (i % 3) * 3.9), Inches(2.2 + (i // 3) * 2.5), Inches(3.6), Inches(2.2), title, b)

    # ---------------- SLIDE 11: FUTURE SCOPE ----------------
    s11 = prs.slides.add_slide(blank_layout)
    set_background(s11)
    add_header(s11, "Future Scope: TruthLens 2.0", "Expanding Capabilities Across Languages, Modalities, and Platforms")
    
    add_card(s11, Inches(0.8), Inches(2.0), w2, Inches(2.3), "Multilingual Detection",
             ["Support for regional languages (Hindi, etc.)", "Combat local misinformation campaigns"])
    add_card(s11, Inches(6.9), Inches(2.0), w2, Inches(2.3), "Multimodal Analysis",
             ["Deepfake image & video verification", "Cross-media forensic consistency checks"])
    add_card(s11, Inches(0.8), Inches(4.6), w2, Inches(2.3), "Browser Extension",
             ["Real-time inline verification overlay", "Flags suspicious headlines inside feeds"])
    add_card(s11, Inches(6.9), Inches(4.6), w2, Inches(2.3), "Source Credibility Index",
             ["Domain registration age & history", "Publisher verification record matching"])

    # ---------------- SLIDE 12: CONCLUSION ----------------
    s12 = prs.slides.add_slide(blank_layout)
    set_background(s12)
    
    t_box12 = s12.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(11.3), Inches(2.5))
    tf12 = t_box12.text_frame
    tf12.word_wrap = True
    
    p = tf12.paragraphs[0]
    p.text = '"Don\'t just read the news. Verify it."'
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p.alignment = PP_ALIGN.CENTER
    
    p2 = tf12.add_paragraph()
    p2.text = "TruthLens – Empowering Society Through Transparent AI"
    p2.font.size = Pt(20)
    p2.font.color.rgb = TEXT_WHITE
    p2.alignment = PP_ALIGN.CENTER

    add_card(s12, Inches(1.5), Inches(4.2), Inches(3.2), Inches(2.2), "Accessible",
             ["Instant analysis", "Runs in any web browser", "Zero hardware barrier"])
    add_card(s12, Inches(5.1), Inches(4.2), Inches(3.2), Inches(2.2), "Explainable",
             ["Keyword influence breakdown", "Uncertainty awareness", "Educational value"])
    add_card(s12, Inches(8.7), Inches(4.2), Inches(3.2), Inches(2.2), "Responsible",
             ["Transparent disclaimers", "Complements journalism", "Promotes critical thinking"])

    prs.save(filename)
    print(f"[SUCCESS] Presentation generated: {filename}")

if __name__ == "__main__":
    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_file = os.path.join(out_dir, "TruthLens_Hackathon_Presentation.pptx")
    create_deck(out_file)
