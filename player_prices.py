# IPL 2026 Complete Player Price Database
# Source: Wikipedia - List of 2026 Indian Premier League personnel changes
# Format: {player_name: {price_cr: float, price_lakh: int, team: str, type: str}}
# type = "retained" | "auction" | "trade" | "replacement"

AUCTION_PRICES = {
    # ═══════════════════════════════════════════════════════════
    # CHENNAI SUPER KINGS (CSK)
    # ═══════════════════════════════════════════════════════════
    "Ruturaj Gaikwad": {"price_cr": 18.00, "team": "CSK", "type": "retained"},
    "Sanju Samson": {"price_cr": 18.00, "team": "CSK", "type": "trade"},
    "Shivam Dube": {"price_cr": 12.00, "team": "CSK", "type": "retained"},
    "Noor Ahmad": {"price_cr": 10.00, "team": "CSK", "type": "retained"},
    "Khaleel Ahmed": {"price_cr": 4.80, "team": "CSK", "type": "retained"},
    "MS Dhoni": {"price_cr": 4.00, "team": "CSK", "type": "retained"},
    "Anshul Kamboj": {"price_cr": 3.40, "team": "CSK", "type": "retained"},
    "Dewald Brevis": {"price_cr": 2.20, "team": "CSK", "type": "retained"},
    "Gurjapneet Singh": {"price_cr": 2.20, "team": "CSK", "type": "retained"},
    "Nathan Ellis": {"price_cr": 2.00, "team": "CSK", "type": "retained"},
    "Jamie Overton": {"price_cr": 1.50, "team": "CSK", "type": "auction"},
    "Prashant Veer": {"price_cr": 14.20, "team": "CSK", "type": "auction"},
    "Kartik Sharma": {"price_cr": 14.20, "team": "CSK", "type": "auction"},
    "Mukesh Choudhary": {"price_cr": 0.30, "team": "CSK", "type": "retained"},
    "Ramakrishna Ghosh": {"price_cr": 0.30, "team": "CSK", "type": "auction"},
    "Shreyas Gopal": {"price_cr": 0.30, "team": "CSK", "type": "auction"},
    "Ayush Mhatre": {"price_cr": 0.30, "team": "CSK", "type": "auction"},
    "Urvil Patel": {"price_cr": 0.30, "team": "CSK", "type": "auction"},

    # ═══════════════════════════════════════════════════════════
    # DELHI CAPITALS (DC)
    # ═══════════════════════════════════════════════════════════
    "Axar Patel": {"price_cr": 16.50, "team": "DC", "type": "retained"},
    "KL Rahul": {"price_cr": 14.00, "team": "DC", "type": "retained"},
    "Kuldeep Yadav": {"price_cr": 13.25, "team": "DC", "type": "retained"},
    "Mitchell Starc": {"price_cr": 11.75, "team": "DC", "type": "retained"},
    "T Natarajan": {"price_cr": 10.75, "team": "DC", "type": "retained"},
    "Tristan Stubbs": {"price_cr": 10.00, "team": "DC", "type": "retained"},
    "Mukesh Kumar": {"price_cr": 8.00, "team": "DC", "type": "retained"},
    "Nitish Rana": {"price_cr": 4.20, "team": "DC", "type": "trade"},
    "Abhishek Porel": {"price_cr": 4.00, "team": "DC", "type": "retained"},
    "Ashutosh Sharma": {"price_cr": 3.80, "team": "DC", "type": "retained"},
    "Sameer Rizvi": {"price_cr": 0.95, "team": "DC", "type": "auction"},
    "Dushmantha Chameera": {"price_cr": 0.75, "team": "DC", "type": "auction"},
    "Karun Nair": {"price_cr": 0.50, "team": "DC", "type": "auction"},
    "Madhav Tiwari": {"price_cr": 0.40, "team": "DC", "type": "auction"},
    "Kyle Jamieson": {"price_cr": 0.75, "team": "DC", "type": "auction"},
    "Ajay Mandal": {"price_cr": 0.30, "team": "DC", "type": "auction"},
    "Tripurana Vijay": {"price_cr": 0.30, "team": "DC", "type": "auction"},
    "Vipraj Nigam": {"price_cr": 0.30, "team": "DC", "type": "auction"},

    # ═══════════════════════════════════════════════════════════
    # GUJARAT TITANS (GT)
    # ═══════════════════════════════════════════════════════════
    "Rashid Khan": {"price_cr": 18.00, "team": "GT", "type": "retained"},
    "Shubman Gill": {"price_cr": 16.50, "team": "GT", "type": "retained"},
    "Jos Buttler": {"price_cr": 15.75, "team": "GT", "type": "retained"},
    "Mohammed Siraj": {"price_cr": 12.25, "team": "GT", "type": "retained"},
    "Kagiso Rabada": {"price_cr": 10.75, "team": "GT", "type": "retained"},
    "Prasidh Krishna": {"price_cr": 9.50, "team": "GT", "type": "retained"},
    "Sai Sudarshan": {"price_cr": 8.50, "team": "GT", "type": "retained"},
    "Rahul Tewatia": {"price_cr": 4.00, "team": "GT", "type": "retained"},
    "Shahrukh Khan": {"price_cr": 4.00, "team": "GT", "type": "retained"},
    "Washington Sundar": {"price_cr": 3.20, "team": "GT", "type": "retained"},
    "Sai Kishore": {"price_cr": 2.00, "team": "GT", "type": "auction"},
    "Glenn Phillips": {"price_cr": 2.00, "team": "GT", "type": "auction"},
    "Arshad Khan": {"price_cr": 1.30, "team": "GT", "type": "auction"},
    "Gurnoor Singh Brar": {"price_cr": 1.30, "team": "GT", "type": "auction"},
    "Ishant Sharma": {"price_cr": 0.75, "team": "GT", "type": "auction"},
    "Jayant Yadav": {"price_cr": 0.75, "team": "GT", "type": "auction"},
    "Kumar Kushagra": {"price_cr": 0.65, "team": "GT", "type": "auction"},
    "Anuj Rawat": {"price_cr": 0.30, "team": "GT", "type": "auction"},
    "Manav Suthar": {"price_cr": 0.30, "team": "GT", "type": "auction"},
    "Nishant Sindhu": {"price_cr": 0.30, "team": "GT", "type": "auction"},

    # ═══════════════════════════════════════════════════════════
    # KOLKATA KNIGHT RIDERS (KKR)
    # ═══════════════════════════════════════════════════════════
    "Cameron Green": {"price_cr": 25.20, "team": "KKR", "type": "auction"},
    "Matheesha Pathirana": {"price_cr": 18.00, "team": "KKR", "type": "auction"},
    "Rinku Singh": {"price_cr": 13.00, "team": "KKR", "type": "retained"},
    "Sunil Narine": {"price_cr": 12.00, "team": "KKR", "type": "retained"},
    "Varun Chakravarthy": {"price_cr": 12.00, "team": "KKR", "type": "retained"},
    "Auqib Nabi Dar": {"price_cr": 8.40, "team": "KKR", "type": "auction"},
    "Harshit Rana": {"price_cr": 4.00, "team": "KKR", "type": "retained"},
    "Ramandeep Singh": {"price_cr": 4.00, "team": "KKR", "type": "retained"},
    "Angkrish Raghuvanshi": {"price_cr": 3.00, "team": "KKR", "type": "retained"},
    "Spencer Johnson": {"price_cr": 2.80, "team": "KKR", "type": "auction"},
    "Ajinkya Rahane": {"price_cr": 1.50, "team": "KKR", "type": "auction"},
    "Rovman Powell": {"price_cr": 1.50, "team": "KKR", "type": "auction"},
    "Vaibhav Arora": {"price_cr": 1.80, "team": "KKR", "type": "retained"},
    "Blessing Muzarabani": {"price_cr": 0.75, "team": "KKR", "type": "replacement"},
    "Saurabh Dubey": {"price_cr": 0.75, "team": "KKR", "type": "replacement"},
    "Manish Pandey": {"price_cr": 0.75, "team": "KKR", "type": "auction"},
    "Umran Malik": {"price_cr": 0.75, "team": "KKR", "type": "auction"},
    "Anukul Roy": {"price_cr": 0.40, "team": "KKR", "type": "auction"},

    # ═══════════════════════════════════════════════════════════
    # LUCKNOW SUPER GIANTS (LSG)
    # ═══════════════════════════════════════════════════════════
    "Rishabh Pant": {"price_cr": 27.00, "team": "LSG", "type": "retained"},
    "Nicholas Pooran": {"price_cr": 21.00, "team": "LSG", "type": "retained"},
    "Mayank Yadav": {"price_cr": 11.00, "team": "LSG", "type": "retained"},
    "Mohammed Shami": {"price_cr": 10.00, "team": "LSG", "type": "trade"},
    "Avesh Khan": {"price_cr": 9.75, "team": "LSG", "type": "retained"},
    "Abdul Samad": {"price_cr": 4.20, "team": "LSG", "type": "retained"},
    "Ayush Badoni": {"price_cr": 4.00, "team": "LSG", "type": "retained"},
    "Mohsin Khan": {"price_cr": 4.00, "team": "LSG", "type": "retained"},
    "Mitchell Marsh": {"price_cr": 3.40, "team": "LSG", "type": "auction"},
    "Shahbaz Ahmed": {"price_cr": 2.40, "team": "LSG", "type": "retained"},
    "Aiden Markram": {"price_cr": 2.00, "team": "LSG", "type": "auction"},
    "Manimaran Siddharth": {"price_cr": 0.75, "team": "LSG", "type": "auction"},
    "Matthew Breetzke": {"price_cr": 0.75, "team": "LSG", "type": "auction"},
    "Akash Singh": {"price_cr": 0.30, "team": "LSG", "type": "auction"},
    "Arjun Tendulkar": {"price_cr": 0.30, "team": "LSG", "type": "trade"},
    "Arshin Kulkarni": {"price_cr": 0.30, "team": "LSG", "type": "auction"},
    "Himmat Singh": {"price_cr": 0.30, "team": "LSG", "type": "auction"},
    "Digvesh Rathi": {"price_cr": 0.30, "team": "LSG", "type": "auction"},
    "Prince Yadav": {"price_cr": 0.30, "team": "LSG", "type": "auction"},

    # ═══════════════════════════════════════════════════════════
    # MUMBAI INDIANS (MI)
    # ═══════════════════════════════════════════════════════════
    "Jasprit Bumrah": {"price_cr": 18.00, "team": "MI", "type": "retained"},
    "Hardik Pandya": {"price_cr": 16.35, "team": "MI", "type": "retained"},
    "Suryakumar Yadav": {"price_cr": 16.35, "team": "MI", "type": "retained"},
    "Rohit Sharma": {"price_cr": 16.30, "team": "MI", "type": "retained"},
    "Trent Boult": {"price_cr": 12.50, "team": "MI", "type": "retained"},
    "Deepak Chahar": {"price_cr": 9.25, "team": "MI", "type": "retained"},
    "Tilak Varma": {"price_cr": 8.00, "team": "MI", "type": "retained"},
    "Will Jacks": {"price_cr": 5.25, "team": "MI", "type": "retained"},
    "Naman Dhir": {"price_cr": 5.25, "team": "MI", "type": "retained"},
    "Allah Ghazanfar": {"price_cr": 4.80, "team": "MI", "type": "retained"},
    "Sherfane Rutherford": {"price_cr": 2.60, "team": "MI", "type": "trade"},
    "Shardul Thakur": {"price_cr": 2.00, "team": "MI", "type": "trade"},
    "Mitchell Santner": {"price_cr": 2.00, "team": "MI", "type": "retained"},
    "Quinton de Kock": {"price_cr": 1.00, "team": "MI", "type": "auction"},
    "Ryan Rickelton": {"price_cr": 1.00, "team": "MI", "type": "auction"},
    "Corbin Bosch": {"price_cr": 0.75, "team": "MI", "type": "auction"},
    "Robin Minz": {"price_cr": 0.65, "team": "MI", "type": "retained"},
    "Raj Angad Bawa": {"price_cr": 0.30, "team": "MI", "type": "retained"},
    "Ashwani Kumar": {"price_cr": 0.30, "team": "MI", "type": "auction"},
    "Raghu Sharma": {"price_cr": 0.30, "team": "MI", "type": "auction"},
    "Mayank Markande": {"price_cr": 0.30, "team": "MI", "type": "trade"},

    # ═══════════════════════════════════════════════════════════
    # PUNJAB KINGS (PBKS)
    # ═══════════════════════════════════════════════════════════
    "Shreyas Iyer": {"price_cr": 26.75, "team": "PBKS", "type": "retained"},
    "Arshdeep Singh": {"price_cr": 18.00, "team": "PBKS", "type": "retained"},
    "Yuzvendra Chahal": {"price_cr": 18.00, "team": "PBKS", "type": "retained"},
    "Marcus Stoinis": {"price_cr": 11.00, "team": "PBKS", "type": "retained"},
    "Marco Jansen": {"price_cr": 7.00, "team": "PBKS", "type": "retained"},
    "Shashank Singh": {"price_cr": 5.50, "team": "PBKS", "type": "retained"},
    "Nehal Wadhera": {"price_cr": 4.20, "team": "PBKS", "type": "retained"},
    "Prabhsimran Singh": {"price_cr": 4.00, "team": "PBKS", "type": "retained"},
    "Priyansh Arya": {"price_cr": 3.80, "team": "PBKS", "type": "retained"},
    "Mitchell Owen": {"price_cr": 3.00, "team": "PBKS", "type": "retained"},
    "Azmatullah Omarzai": {"price_cr": 2.40, "team": "PBKS", "type": "retained"},
    "Lockie Ferguson": {"price_cr": 2.00, "team": "PBKS", "type": "auction"},
    "Vijaykumar Vyshak": {"price_cr": 1.80, "team": "PBKS", "type": "retained"},
    "Yash Thakur": {"price_cr": 1.60, "team": "PBKS", "type": "retained"},
    "Harpreet Brar": {"price_cr": 1.50, "team": "PBKS", "type": "retained"},
    "Vishnu Vinod": {"price_cr": 0.95, "team": "PBKS", "type": "auction"},
    "Xavier Bartlett": {"price_cr": 0.80, "team": "PBKS", "type": "auction"},
    "Pyla Avinash": {"price_cr": 0.30, "team": "PBKS", "type": "auction"},
    "Harnoor Pannu": {"price_cr": 0.30, "team": "PBKS", "type": "retained"},
    "Musheer Khan": {"price_cr": 0.30, "team": "PBKS", "type": "auction"},
    "Suryansh Shedge": {"price_cr": 0.30, "team": "PBKS", "type": "retained"},

    # ═══════════════════════════════════════════════════════════
    # RAJASTHAN ROYALS (RR)
    # ═══════════════════════════════════════════════════════════
    "Yashasvi Jaiswal": {"price_cr": 18.00, "team": "RR", "type": "retained"},
    "Riyan Parag": {"price_cr": 14.00, "team": "RR", "type": "retained"},
    "Ravindra Jadeja": {"price_cr": 14.00, "team": "RR", "type": "trade"},
    "Dhruv Jurel": {"price_cr": 14.00, "team": "RR", "type": "retained"},
    "Jofra Archer": {"price_cr": 12.50, "team": "RR", "type": "retained"},
    "Shimron Hetmyer": {"price_cr": 11.00, "team": "RR", "type": "retained"},
    "Ravi Bishnoi": {"price_cr": 7.20, "team": "RR", "type": "auction"},
    "Tushar Deshpande": {"price_cr": 6.50, "team": "RR", "type": "retained"},
    "Sandeep Sharma": {"price_cr": 4.00, "team": "RR", "type": "retained"},
    "Nandre Burger": {"price_cr": 3.50, "team": "RR", "type": "retained"},
    "Prithvi Shaw": {"price_cr": 3.20, "team": "RR", "type": "auction"},
    "Sam Curran": {"price_cr": 2.40, "team": "RR", "type": "trade"},
    "Kwena Maphaka": {"price_cr": 1.50, "team": "RR", "type": "auction"},
    "Vaibhav Sooryavanshi": {"price_cr": 1.10, "team": "RR", "type": "retained"},
    "Donovan Ferreira": {"price_cr": 1.00, "team": "RR", "type": "trade"},
    "Shubham Dubey": {"price_cr": 0.80, "team": "RR", "type": "auction"},
    "Yudhvir Singh": {"price_cr": 0.35, "team": "RR", "type": "auction"},
    "Lhuan-dre Pretorius": {"price_cr": 0.30, "team": "RR", "type": "auction"},

    # ═══════════════════════════════════════════════════════════
    # ROYAL CHALLENGERS BENGALURU (RCB)
    # ═══════════════════════════════════════════════════════════
    "Virat Kohli": {"price_cr": 21.00, "team": "RCB", "type": "retained"},
    "Josh Hazlewood": {"price_cr": 12.50, "team": "RCB", "type": "retained"},
    "Phil Salt": {"price_cr": 11.50, "team": "RCB", "type": "retained"},
    "Rajat Patidar": {"price_cr": 11.00, "team": "RCB", "type": "retained"},
    "Jitesh Sharma": {"price_cr": 11.00, "team": "RCB", "type": "retained"},
    "Bhuvneshwar Kumar": {"price_cr": 10.75, "team": "RCB", "type": "retained"},
    "Venkatesh Iyer": {"price_cr": 7.00, "team": "RCB", "type": "auction"},
    "Rasikh Salam": {"price_cr": 6.00, "team": "RCB", "type": "retained"},
    "Krunal Pandya": {"price_cr": 5.75, "team": "RCB", "type": "retained"},
    "Yash Dayal": {"price_cr": 5.00, "team": "RCB", "type": "retained"},
    "Suyash Sharma": {"price_cr": 4.50, "team": "RCB", "type": "auction"},
    "Tim David": {"price_cr": 3.00, "team": "RCB", "type": "retained"},
    "Jacob Bethell": {"price_cr": 2.60, "team": "RCB", "type": "auction"},
    "Devdutt Padikkal": {"price_cr": 2.00, "team": "RCB", "type": "retained"},
    "Nuwan Thushara": {"price_cr": 1.60, "team": "RCB", "type": "auction"},
    "Romario Shepherd": {"price_cr": 1.50, "team": "RCB", "type": "auction"},
    "Swapnil Singh": {"price_cr": 0.50, "team": "RCB", "type": "auction"},
    "Abhinandan Singh": {"price_cr": 0.30, "team": "RCB", "type": "auction"},

    # ═══════════════════════════════════════════════════════════
    # SUNRISERS HYDERABAD (SRH)
    # ═══════════════════════════════════════════════════════════
    "Heinrich Klaasen": {"price_cr": 23.00, "team": "SRH", "type": "retained"},
    "Pat Cummins": {"price_cr": 18.00, "team": "SRH", "type": "retained"},
    "Travis Head": {"price_cr": 14.00, "team": "SRH", "type": "retained"},
    "Abhishek Sharma": {"price_cr": 14.00, "team": "SRH", "type": "retained"},
    "Ishan Kishan": {"price_cr": 11.25, "team": "SRH", "type": "retained"},
    "Harshal Patel": {"price_cr": 8.00, "team": "SRH", "type": "retained"},
    "Nitish Kumar Reddy": {"price_cr": 6.00, "team": "SRH", "type": "retained"},
    "Eshan Malinga": {"price_cr": 1.20, "team": "SRH", "type": "auction"},
    "Brydon Carse": {"price_cr": 1.00, "team": "SRH", "type": "auction"},
    "Jaydev Unadkat": {"price_cr": 1.00, "team": "SRH", "type": "auction"},
    "Kamindu Mendis": {"price_cr": 0.75, "team": "SRH", "type": "auction"},
    "Atharva Taide": {"price_cr": 0.50, "team": "SRH", "type": "auction"},
    "Zeeshan Ansari": {"price_cr": 0.40, "team": "SRH", "type": "retained"},
    "Smaran Ravichandran": {"price_cr": 0.30, "team": "SRH", "type": "auction"},
    "Aniket Verma": {"price_cr": 0.30, "team": "SRH", "type": "auction"},
    "Harsh Dubey": {"price_cr": 0.30, "team": "SRH", "type": "auction"},
}
