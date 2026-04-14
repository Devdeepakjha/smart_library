def cover(isbn):
    return f"https://covers.openlibrary.org/b/isbn/{isbn}-M.jpg"


def build_seed_books():
    # Categories with around 12 books each (seed data)
    # ISBNs are used only for cover URLs (Open Library provides a reliable response).
    data = []

    def add(category, title, author, isbn, description, summary):
        data.append(
            {
                "category": category,
                "title": title,
                "author": author,
                "cover_image": cover(isbn),
                "description": description,
                "summary": summary,
            }
        )

    # Manga
    add("Manga", "Naruto, Vol. 1", "Masashi Kishimoto", "9781569319000",
        "A young ninja dreams of becoming the strongest leader of his village.",
        "Naruto begins his journey, facing early rivals and learning what it means to be acknowledged.")
    add("Manga", "One Piece, Vol. 1", "Eiichiro Oda", "9781569319017",
        "A rubber-powered pirate sets sail to find the legendary treasure.",
        "Luffy forms his first crew connections and begins the grand adventure on the seas.")
    add("Manga", "Death Note, Vol. 1", "Tsugumi Ohba", "9781421501680",
        "A notebook gives its owner the power to kill by writing a name.",
        "Light tests the notebook and a deadly mind game starts with a mysterious detective.")
    add("Manga", "Attack on Titan, Vol. 1", "Hajime Isayama", "9781612620244",
        "Humanity hides behind walls from terrifying Titans.",
        "Eren’s world collapses after an attack, pushing him toward a vow of revenge.")
    add("Manga", "Demon Slayer, Vol. 1", "Koyoharu Gotouge", "9781974700523",
        "A boy becomes a demon slayer to save his sister.",
        "Tanjiro begins training and meets allies as he fights to restore his family.")
    add("Manga", "My Hero Academia, Vol. 1", "Kohei Horikoshi", "9781421582696",
        "In a world of superpowers, a boy without powers wants to be a hero.",
        "Izuku gets a chance to inherit a power and step into a hero academy.")
    add("Manga", "Tokyo Ghoul, Vol. 1", "Sui Ishida", "9781421580364",
        "A college student becomes part-ghoul after a tragic event.",
        "Kaneki struggles with identity and survival in a city where ghouls hide in plain sight.")
    add("Manga", "Fullmetal Alchemist, Vol. 1", "Hiromu Arakawa", "9781591169208",
        "Two brothers use alchemy to undo a terrible mistake.",
        "The Elric brothers search for the Philosopher’s Stone while facing the costs of ambition.")
    add("Manga", "Bleach, Vol. 1", "Tite Kubo", "9781591164418",
        "A teenager gains the powers of a Soul Reaper.",
        "Ichigo protects his town from spirits and begins a new duty between worlds.")
    add("Manga", "Jujutsu Kaisen, Vol. 1", "Gege Akutami", "9781974710027",
        "A student enters a world of curses after swallowing a cursed object.",
        "Yuji joins a sorcery school and learns to fight dangerous spirits.")
    add("Manga", "Haikyuu!!, Vol. 1", "Haruichi Furudate", "9781421587660",
        "A short boy aims to become a great volleyball player.",
        "Hinata joins a team and learns teamwork, practice, and rivalry on the court.")
    add("Manga", "Spy x Family, Vol. 1", "Tatsuya Endo", "9781974715466",
        "A spy builds a fake family for a mission, unknowingly with secrets.",
        "Twilight’s mission becomes complicated with a telepath child and an assassin wife.")

    # Romance
    add("Romance", "Pride and Prejudice", "Jane Austen", "9780141439518",
        "A classic story of love, class, and misunderstandings in England.",
        "Elizabeth and Darcy clash and grow, learning humility and honesty.")
    add("Romance", "Jane Eyre", "Charlotte Brontë", "9780141441146",
        "An orphaned girl becomes a governess and finds love with secrets.",
        "Jane insists on dignity and independence while uncovering Rochester’s hidden past.")
    add("Romance", "Me Before You", "Jojo Moyes", "9780143124542",
        "A caretaker and a man in a wheelchair change each other’s lives.",
        "Louisa discovers purpose while Will challenges her to live boldly.")
    add("Romance", "The Notebook", "Nicholas Sparks", "9780446605236",
        "A timeless love story remembered across years.",
        "Noah and Allie’s romance survives distance, choices, and time.")
    add("Romance", "Outlander", "Diana Gabaldon", "9780440212560",
        "A nurse is transported to 18th-century Scotland.",
        "Claire faces danger and love as she adapts to a new time and identity.")
    add("Romance", "The Time Traveler's Wife", "Audrey Niffenegger", "9780156029438",
        "A love story affected by unpredictable time travel.",
        "Clare and Henry navigate commitment while time keeps pulling them apart.")
    add("Romance", "The Rosie Project", "Graeme Simsion", "9781476729091",
        "A socially awkward professor creates a plan to find a wife.",
        "Don’s project fails beautifully when he meets Rosie and learns flexibility.")
    add("Romance", "The Fault in Our Stars", "John Green", "9780525478812",
        "Two teens with cancer fall in love and seek meaning.",
        "Hazel and Gus share a deep bond and a trip that changes their perspective.")
    add("Romance", "Love in the Time of Cholera", "Gabriel García Márquez", "9780307389732",
        "A man waits decades for his chance at love.",
        "Florentino’s devotion is tested by time, society, and real human complexity.")
    add("Romance", "Eleanor & Park", "Rainbow Rowell", "9781250012579",
        "Two misfit teens connect through music and comics.",
        "Eleanor and Park find comfort in each other while facing tough realities.")
    add("Romance", "Twilight", "Stephenie Meyer", "9780316015844",
        "A teen falls in love with a mysterious vampire.",
        "Bella enters a dangerous world where love brings both risk and loyalty.")
    add("Romance", "It Ends with Us", "Colleen Hoover", "9781501110368",
        "A woman faces hard truths about love and patterns.",
        "Lily’s choices show that love alone isn’t always enough to stay safe.")

    # Education
    add("Education", "How to Study", "Ron Fry", "9781564140364",
        "Practical tips to improve study habits and exam performance.",
        "Simple methods for focus, notes, memory, and planning study time.")
    add("Education", "Make It Stick", "Peter C. Brown", "9780674729018",
        "Learning science made practical for students and teachers.",
        "Explains why practice, recall, and spacing beat cramming.")
    add("Education", "Mindset", "Carol S. Dweck", "9780345472328",
        "How beliefs about ability affect learning and success.",
        "A growth mindset helps students improve through effort and strategy.")
    add("Education", "Atomic Habits", "James Clear", "9780735211292",
        "Build good habits with small changes and consistency.",
        "Focus on systems, identity, and simple routines to improve daily learning.")
    add("Education", "Deep Work", "Cal Newport", "9781455586691",
        "Rules for focused success in a distracted world.",
        "Shows how to build concentration and reduce shallow work.")
    add("Education", "The Power of Habit", "Charles Duhigg", "9780812981605",
        "How habits work and how to change them.",
        "Understanding cues and rewards helps improve study routines.")
    add("Education", "Grit", "Angela Duckworth", "9781501111105",
        "Why passion and perseverance matter more than talent.",
        "Explains how long-term effort shapes achievement.")
    add("Education", "A Mind for Numbers", "Barbara Oakley", "9780399165245",
        "Learning math and science with practical techniques.",
        "Simple tools to beat procrastination and understand tough concepts.")
    add("Education", "The 7 Habits of Highly Effective People", "Stephen R. Covey", "9780743269513",
        "Personal development habits for students and professionals.",
        "Helps plan goals, manage time, and build effective relationships.")
    add("Education", "Thinking, Fast and Slow", "Daniel Kahneman", "9780374533557",
        "How the mind makes decisions and mistakes.",
        "Explains two thinking systems and how to avoid common learning biases.")
    add("Education", "Learning How to Learn", "Barbara Oakley", "9780143131090",
        "Study strategies for all kinds of learners.",
        "Covers focus modes, memory tricks, and effective practice.")
    add("Education", "The Art of Learning", "Josh Waitzkin", "9780743277464",
        "Lessons on learning from chess and martial arts.",
        "Shows how mindset and practice help master any skill.")

    # Rom-Com
    add("Rom-Com", "Can You Keep a Secret?", "Sophie Kinsella", "9780440241416",
        "A woman shares her secrets with a stranger—who isn’t a stranger.",
        "Emma’s life gets funny and messy when her secrets return in the form of her boss.")
    add("Rom-Com", "Bridget Jones's Diary", "Helen Fielding", "9780140280098",
        "A funny diary of love, self-image, and awkward moments.",
        "Bridget navigates relationships while learning to accept herself.")
    add("Rom-Com", "The Unhoneymooners", "Christina Lauren", "9781501128035",
        "Two enemies take a honeymoon trip together.",
        "Olive and Ethan fake being a couple and slowly become real.")
    add("Rom-Com", "The Hating Game", "Sally Thorne", "9780062439598",
        "Office rivals compete—and feelings show up.",
        "Lucy and Joshua’s rivalry turns into romance with plenty of banter.")
    add("Rom-Com", "Red, White & Royal Blue", "Casey McQuiston", "9781250316776",
        "A prince and the president’s son fall for each other.",
        "Public image clashes with private feelings as a romance grows.")
    add("Rom-Com", "Love, Rosie", "Cecelia Ahern", "9780786890755",
        "Best friends miss chances at love through life.",
        "Rosie and Alex’s story shows timing, friendship, and regret in a sweet way.")
    add("Rom-Com", "People We Meet on Vacation", "Emily Henry", "9781984806758",
        "Two friends travel every year until something breaks.",
        "They revisit old trips to fix what went wrong and admit feelings.")
    add("Rom-Com", "Beach Read", "Emily Henry", "9781984806734",
        "Two writers swap genres and swap feelings too.",
        "A summer challenge becomes personal as they help each other heal.")
    add("Rom-Com", "To All the Boys I've Loved Before", "Jenny Han", "9781442426719",
        "A girl’s secret love letters get mailed accidentally.",
        "Lara Jean’s fake relationship turns into real emotions.")
    add("Rom-Com", "Crazy Rich Asians", "Kevin Kwan", "9780385536974",
        "A woman meets her boyfriend’s super-rich family.",
        "Rachel faces culture shock, judgment, and unexpected allies.")
    add("Rom-Com", "The Kiss Quotient", "Helen Hoang", "9780451490803",
        "A woman hires an escort to practice dating.",
        "Stella and Michael build trust, respect, and real love.")
    add("Rom-Com", "The Flatshare", "Beth O'Leary", "9781250193674",
        "Two strangers share a flat at different times.",
        "They fall for each other through notes and small kindness.")

    # Sitcom (TV-inspired light reads / humor)
    add("Sitcom", "Bossypants", "Tina Fey", "9780316056861",
        "Funny memoir with stories from TV and life.",
        "Tina shares lessons about work, confidence, and mistakes with humor.")
    add("Sitcom", "Yes Please", "Amy Poehler", "9780062268341",
        "A mix of comedy, stories, and advice.",
        "Amy writes about career, friendships, and being brave in a fun way.")
    add("Sitcom", "Is Everyone Hanging Out Without Me?", "Mindy Kaling", "9780307886279",
        "Comedy essays about growing up and show business.",
        "Mindy’s honest humor makes everyday awkward moments feel relatable.")
    add("Sitcom", "Born a Crime", "Trevor Noah", "9780399588198",
        "A funny and powerful memoir from South Africa.",
        "Trevor’s childhood stories mix comedy with real social lessons.")
    add("Sitcom", "The Office: The Untold Story", "Andy Greene", "9781524744975",
        "Behind-the-scenes stories from a famous comedy show.",
        "Cast and creators share how the show was made and why it worked.")
    add("Sitcom", "The Simpsons and Philosophy", "William Irwin", "9780812694338",
        "Philosophy explained through famous cartoon episodes.",
        "Fun examples show how big ideas can be understood simply.")
    add("Sitcom", "Friends, Lovers and the Big Terrible Thing", "Matthew Perry", "9781250866448",
        "Memoir about fame and personal struggles.",
        "A candid story showing how comedy can hide real life challenges.")
    add("Sitcom", "Modern Family: The Companion", "Steve Mallory", "9781780977856",
        "A light companion guide to a popular sitcom.",
        "Quick facts and moments that highlight family humor and warmth.")
    add("Sitcom", "Seinfeld and Philosophy", "William Irwin", "9780812694611",
        "Thinking about everyday life through a comedy lens.",
        "Shows how small situations can teach big lessons.")
    add("Sitcom", "The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "9780345391803",
        "A sci-fi comedy full of absurd adventures.",
        "Arthur’s journey is chaotic, funny, and surprisingly thoughtful.")
    add("Sitcom", "Good Omens", "Neil Gaiman & Terry Pratchett", "9780060853983",
        "An angel and demon try to stop the apocalypse.",
        "A witty story about friendship, fate, and doing the right thing.")
    add("Sitcom", "Three Men in a Boat", "Jerome K. Jerome", "9780141441214",
        "Classic humor about a boating trip gone silly.",
        "Simple jokes and funny situations make it an easy, enjoyable read.")

    # CSE
    add("CSE", "Let Us C", "Yashavant Kanetkar", "9788183331630",
        "A beginner-friendly introduction to C programming.",
        "C basics explained with examples, helping build strong fundamentals.")
    add("CSE", "Python Crash Course", "Eric Matthes", "9781593276034",
        "A fast-paced introduction to Python.",
        "Covers syntax, projects, and practice ideas for beginners.")
    add("CSE", "Automate the Boring Stuff with Python", "Al Sweigart", "9781593275990",
        "Practical Python for everyday tasks.",
        "Shows how to automate simple jobs and build confidence.")
    add("CSE", "Head First Java", "Kathy Sierra", "9780596009205",
        "Java basics with a friendly style.",
        "Builds core OOP understanding through simple examples.")
    add("CSE", "Database System Concepts", "Silberschatz, Korth", "9780073523323",
        "Foundations of DBMS for students.",
        "Explains tables, queries, and transactions with clarity.")
    add("CSE", "Operating System Concepts", "Silberschatz, Galvin", "9781119800361",
        "Core concepts of operating systems.",
        "Processes, memory, and scheduling explained for learners.")
    add("CSE", "Computer Networks", "Andrew S. Tanenbaum", "9780132126953",
        "Networking fundamentals in a clear style.",
        "Covers layers, protocols, and real examples.")
    add("CSE", "Clean Code", "Robert C. Martin", "9780132350884",
        "How to write readable, maintainable code.",
        "Simple principles that improve code quality and teamwork.")
    add("CSE", "The Pragmatic Programmer", "Andrew Hunt", "9780201616224",
        "Practical advice for software developers.",
        "Helps students think like professionals with habits and best practices.")
    add("CSE", "Introduction to Algorithms", "Cormen, Leiserson", "9780262033848",
        "A standard algorithms book for CS.",
        "Explains important algorithms and how to analyze them.")
    add("CSE", "Eloquent JavaScript", "Marijn Haverbeke", "9781593279509",
        "Modern JavaScript fundamentals.",
        "Covers JS basics, DOM, and clean coding approaches.")
    add("CSE", "Flask Web Development", "Miguel Grinberg", "9781491991732",
        "Building web apps using Flask.",
        "Shows routing, templates, and database basics in an easy style.")

    # Fiction
    add("Fiction", "To Kill a Mockingbird", "Harper Lee", "9780061120084",
        "A child’s view of justice and racism in a small town.",
        "Scout learns about empathy and courage through her father’s case.")
    add("Fiction", "1984", "George Orwell", "9780451524935",
        "A dystopian society controlled by surveillance and fear.",
        "Winston’s rebellion shows the cost of truth under oppression.")
    add("Fiction", "The Great Gatsby", "F. Scott Fitzgerald", "9780743273565",
        "A story of wealth, dreams, and disappointment.",
        "Gatsby’s obsession reveals how fragile dreams can be.")
    add("Fiction", "The Catcher in the Rye", "J. D. Salinger", "9780316769488",
        "A teen struggles with growing up and loneliness.",
        "Holden’s voice captures confusion and search for meaning.")
    add("Fiction", "The Alchemist", "Paulo Coelho", "9780061122415",
        "A shepherd follows a dream to find treasure.",
        "A simple journey about purpose, courage, and listening to your heart.")
    add("Fiction", "The Kite Runner", "Khaled Hosseini", "9781594631931",
        "Friendship and guilt set against Afghanistan’s history.",
        "Atonement and loyalty drive a powerful personal story.")
    add("Fiction", "The Book Thief", "Markus Zusak", "9780375842207",
        "A girl finds comfort in books during WWII Germany.",
        "Words become both shelter and power in a hard time.")
    add("Fiction", "Life of Pi", "Yann Martel", "9780156027328",
        "A boy survives at sea with a tiger.",
        "A survival tale that blends faith, fear, and imagination.")
    add("Fiction", "The Road", "Cormac McCarthy", "9780307387894",
        "A father and son travel through a ruined world.",
        "A quiet, intense story about love and survival.")
    add("Fiction", "The Hobbit", "J. R. R. Tolkien", "9780547928227",
        "A simple hobbit goes on an unexpected adventure.",
        "Bilbo faces danger and grows into bravery.")
    add("Fiction", "The Da Vinci Code", "Dan Brown", "9780307474273",
        "A thriller based on art, secrets, and puzzles.",
        "A fast chase reveals hidden clues and controversial theories.")
    add("Fiction", "A Thousand Splendid Suns", "Khaled Hosseini", "9781594489501",
        "Two women form a bond under hardship.",
        "Their friendship becomes strength in a difficult life.")

    # Non-Fiction
    add("Non-Fiction", "Sapiens", "Yuval Noah Harari", "9780062316097",
        "A brief history of humankind.",
        "Explains how humans evolved and built societies through shared stories.")
    add("Non-Fiction", "Educated", "Tara Westover", "9780399590504",
        "A memoir about growing up outside formal education.",
        "Tara’s journey shows how learning can change identity and freedom.")
    add("Non-Fiction", "The Immortal Life of Henrietta Lacks", "Rebecca Skloot", "9781400052189",
        "The story behind famous cells used in research.",
        "Shows ethics, science, and a family’s untold history.")
    add("Non-Fiction", "Quiet", "Susan Cain", "9780307352151",
        "The power of introverts in a loud world.",
        "Explains how quiet strengths matter in school and work.")
    add("Non-Fiction", "Outliers", "Malcolm Gladwell", "9780316017930",
        "What makes high achievers different.",
        "Success is shaped by opportunity, practice, and timing.")
    add("Non-Fiction", "Freakonomics", "Steven D. Levitt", "9780061234002",
        "Economics explained through surprising questions.",
        "Shows how incentives affect behavior in real life.")
    add("Non-Fiction", "Into the Wild", "Jon Krakauer", "9780385486804",
        "A young man’s risky journey into Alaska.",
        "A story about freedom, choices, and consequences.")
    add("Non-Fiction", "The Wright Brothers", "David McCullough", "9781476728759",
        "How two brothers built the first airplane.",
        "Persistence and teamwork turn an idea into history.")
    add("Non-Fiction", "The Tipping Point", "Malcolm Gladwell", "9780316346627",
        "How small changes create big social shifts.",
        "Explains how ideas spread and become popular.")
    add("Non-Fiction", "When Breath Becomes Air", "Paul Kalanithi", "9780812988406",
        "A neurosurgeon reflects on life and death.",
        "A moving story about meaning, purpose, and mortality.")
    add("Non-Fiction", "A Brief History of Time", "Stephen Hawking", "9780553380163",
        "Big questions about the universe explained simply.",
        "Time, space, and black holes made approachable.")
    add("Non-Fiction", "The Power of Now", "Eckhart Tolle", "9781577314806",
        "A guide to mindfulness and living in the present.",
        "Focus on the present moment to reduce stress and improve clarity.")

    # Self-Help
    add("Self-Help", "How to Win Friends and Influence People", "Dale Carnegie", "9780671027032",
        "Classic advice for communication and relationships.",
        "Simple principles for listening, respect, and positive influence.")
    add("Self-Help", "The Subtle Art of Not Giving a F*ck", "Mark Manson", "9780062457714",
        "A blunt approach to values and priorities.",
        "Focus on what matters, accept limits, and live honestly.")
    add("Self-Help", "Ikigai", "Héctor García", "9780143130727",
        "A Japanese concept of purpose and long life.",
        "Small habits and meaning can create a satisfying daily routine.")
    add("Self-Help", "The 5 AM Club", "Robin Sharma", "9781443456623",
        "A routine-focused approach to productivity.",
        "Early mornings are used for learning, planning, and self-growth.")
    add("Self-Help", "Eat That Frog!", "Brian Tracy", "9781626569410",
        "Stop procrastinating with simple priority methods.",
        "Do the hardest task first to build momentum.")
    add("Self-Help", "Who Moved My Cheese?", "Spencer Johnson", "9780091816971",
        "A short story about dealing with change.",
        "Adapt quickly and keep moving instead of fearing change.")
    add("Self-Help", "The Magic of Thinking Big", "David J. Schwartz", "9780671646783",
        "Build confidence and aim higher.",
        "Thinking bigger helps improve actions and results.")
    add("Self-Help", "Think Like a Monk", "Jay Shetty", "9781982134488",
        "Lessons on calm, purpose, and discipline.",
        "Simple ideas to reduce negativity and build better habits.")
    add("Self-Help", "The Four Agreements", "Don Miguel Ruiz", "9781878424310",
        "Four simple principles for a peaceful life.",
        "Be truthful, don’t assume, and do your best.")
    add("Self-Help", "The Psychology of Money", "Morgan Housel", "9780857197689",
        "How behavior affects financial decisions.",
        "Money choices are emotional; patience and simplicity win long-term.")
    add("Self-Help", "The Alchemist (Life Lessons)", "Paulo Coelho", "9780061122415",
        "A simple story often used for motivation.",
        "Follow your purpose and learn from your journey.")
    add("Self-Help", "Man's Search for Meaning", "Viktor E. Frankl", "9780807014271",
        "A powerful book about meaning in difficult times.",
        "Purpose and mindset help people survive and rebuild.")

    # Biography
    add("Biography", "Steve Jobs", "Walter Isaacson", "9781451648539",
        "The life of Apple’s co-founder.",
        "Shows creativity, leadership, and the cost of perfection.")
    add("Biography", "Long Walk to Freedom", "Nelson Mandela", "9780316548182",
        "Mandela’s journey from prisoner to leader.",
        "A story of courage, sacrifice, and hope.")
    add("Biography", "Wings of Fire", "A. P. J. Abdul Kalam", "9788173711466",
        "The inspiring story of India’s missile man.",
        "Kalam’s life shows discipline, learning, and national service.")
    add("Biography", "The Diary of a Young Girl", "Anne Frank", "9780553296983",
        "A teenager’s diary during WWII.",
        "Anne’s voice shows hope and humanity under fear.")
    add("Biography", "I Am Malala", "Malala Yousafzai", "9780316322409",
        "A girl fights for education and survives an attack.",
        "Malala’s story highlights courage and the value of schooling.")
    add("Biography", "Becoming", "Michelle Obama", "9781524763136",
        "A memoir of identity, work, and family.",
        "Honest reflections about growth, confidence, and public life.")
    add("Biography", "Einstein: His Life and Universe", "Walter Isaacson", "9780743264747",
        "Biography of a scientific genius.",
        "Explains Einstein’s curiosity and how ideas changed science.")
    add("Biography", "Shoe Dog", "Phil Knight", "9781501135910",
        "The story of building Nike.",
        "A business journey full of risk, failure, and persistence.")
    add("Biography", "Into the Heart of Life", "Deepak Chopra", "9780553379730",
        "Reflections on life and well-being.",
        "Simple ideas about health, purpose, and calm.")
    add("Biography", "Elon Musk", "Ashlee Vance", "9780062301239",
        "A biography of a modern tech entrepreneur.",
        "Shows ambition, innovation, and the chaos behind big goals.")
    add("Biography", "The Story of My Experiments with Truth", "Mahatma Gandhi", "9780143052203",
        "Gandhi’s autobiography and personal growth.",
        "Truth, discipline, and non-violence shape his life choices.")
    add("Biography", "Playing It My Way", "Sachin Tendulkar", "9781473605176",
        "Cricket legend’s life story and career.",
        "Hard work and focus turn talent into greatness.")

    # Science
    add("Science", "Cosmos", "Carl Sagan", "9780345539434",
        "A classic introduction to space and science.",
        "Explains the universe with wonder and simple storytelling.")
    add("Science", "The Gene", "Siddhartha Mukherjee", "9781476733524",
        "A history of genetics and its impact.",
        "Shows how genes work and why ethics matter.")
    add("Science", "The Selfish Gene", "Richard Dawkins", "9780199291151",
        "Evolution explained through genes.",
        "Shows how natural selection shapes behavior and life.")
    add("Science", "The Body", "Bill Bryson", "9780385539300",
        "A tour of the human body in a fun way.",
        "Explains how our body works with surprising facts.")
    add("Science", "Brief Answers to the Big Questions", "Stephen Hawking", "9781984819192",
        "Simple answers to big science questions.",
        "Covers space, time, AI, and the future.")
    add("Science", "The Elegant Universe", "Brian Greene", "9780393338102",
        "String theory and modern physics in simple words.",
        "Explains how scientists try to unite physics ideas.")
    add("Science", "A Short History of Nearly Everything", "Bill Bryson", "9780767908184",
        "Science history made enjoyable.",
        "From atoms to dinosaurs, it explains how we know what we know.")
    add("Science", "The Double Helix", "James D. Watson", "9780743216302",
        "How DNA was discovered.",
        "A personal story of competition, mistakes, and discovery.")
    add("Science", "The Sixth Extinction", "Elizabeth Kolbert", "9781250062185",
        "How human activity affects species.",
        "Shows evidence and stories about extinctions happening today.")
    add("Science", "Silent Spring", "Rachel Carson", "9780618249060",
        "A book that changed environmental awareness.",
        "Explains the effects of chemicals on nature.")
    add("Science", "The Origin of Species", "Charles Darwin", "9781509827695",
        "A foundational work on evolution.",
        "Natural selection explains how species change over time.")
    add("Science", "The Martian", "Andy Weir", "9780553418026",
        "A science-based survival story on Mars.",
        "A stranded astronaut uses problem-solving to stay alive.")

    # Technology
    add("Technology", "The Innovators", "Walter Isaacson", "9781476708706",
        "How computers and the internet were built.",
        "Shows teamwork behind major inventions.")
    add("Technology", "The Phoenix Project", "Gene Kim", "9780988262591",
        "A story about fixing IT problems in a company.",
        "Explains DevOps ideas using a simple novel style.")
    add("Technology", "Hooked", "Nir Eyal", "9781591847786",
        "How products create user habits.",
        "A simple model for building engaging apps responsibly.")
    add("Technology", "Don't Make Me Think", "Steve Krug", "9780321965516",
        "Usability basics for websites.",
        "Make interfaces obvious so users don’t struggle.")
    add("Technology", "Cracking the Coding Interview", "Gayle Laakmann McDowell", "9780984782857",
        "Interview practice for programmers.",
        "Common problems and clear solutions for coding interviews.")
    add("Technology", "The Clean Coder", "Robert C. Martin", "9780137081073",
        "Professional habits for programmers.",
        "Focus on responsibility, communication, and quality.")
    add("Technology", "Design of Everyday Things", "Don Norman", "9780465050659",
        "Why design matters in daily objects and apps.",
        "Good design reduces mistakes and makes usage simple.")
    add("Technology", "Code", "Charles Petzold", "9780735611313",
        "How computers work from basic ideas.",
        "Explains logic and hardware in an easy, step-by-step way.")
    add("Technology", "The Cathedral and the Bazaar", "Eric S. Raymond", "9780596001087",
        "Open-source development ideas.",
        "Shows how community building can improve software.")
    add("Technology", "You Don't Know JS Yet", "Kyle Simpson", "9781091210096",
        "Deepen JavaScript understanding.",
        "Explains core JS concepts in a practical way.")
    add("Technology", "Refactoring", "Martin Fowler", "9780201485677",
        "Improving code without changing behavior.",
        "Small steps to keep code clean and maintainable.")
    add("Technology", "The Art of Computer Programming", "Donald Knuth", "9780201896831",
        "A famous reference for algorithms and computation.",
        "Shows deep thinking about programming and problem-solving.")

    # History
    add("History", "Guns, Germs, and Steel", "Jared Diamond", "9780393317558",
        "Why some societies advanced faster than others.",
        "Geography and resources shaped history more than talent.")
    add("History", "A People's History of the United States", "Howard Zinn", "9780062397348",
        "History told from common people’s view.",
        "Focuses on workers, movements, and overlooked voices.")
    add("History", "The Silk Roads", "Peter Frankopan", "9781101912379",
        "History of trade routes and empires.",
        "Shows how Asia and Europe influenced each other through trade.")
    add("History", "The Diary of Samuel Pepys (Selections)", "Samuel Pepys", "9780140436143",
        "A firsthand look at 17th-century London.",
        "Daily life, politics, and events told through diary entries.")
    add("History", "The Crusades", "Thomas Asbridge", "9780060889135",
        "A clear history of the Crusades.",
        "Explains causes, major events, and long-term impact.")
    add("History", "SPQR", "Mary Beard", "9781631492228",
        "A history of ancient Rome.",
        "Shows how Rome grew and why it lasted so long.")
    add("History", "The Cold War", "John Lewis Gaddis", "9780143038276",
        "A readable overview of the Cold War.",
        "Explains tensions, events, and outcomes between major powers.")
    add("History", "India After Gandhi", "Ramachandra Guha", "9780060958589",
        "Modern history of India after independence.",
        "Politics, society, and key events explained with detail.")
    add("History", "The Wright Brothers (History)", "David McCullough", "9781476728759",
        "How flight changed the modern world.",
        "A focused story of innovation that became history.")
    add("History", "The Second World War", "Antony Beevor", "9780316023740",
        "A broad overview of WWII events.",
        "Explains major battles and the human cost of war.")
    add("History", "The Story of Civilization (Selections)", "Will Durant", "9780671017033",
        "A readable collection of world history highlights.",
        "Big events and ideas presented as a narrative.")
    add("History", "The Rise and Fall of the Third Reich", "William L. Shirer", "9781451651683",
        "A detailed account of Nazi Germany.",
        "Shows how the regime rose and the consequences that followed.")

    # Philosophy
    add("Philosophy", "Meditations", "Marcus Aurelius", "9780140449334",
        "Personal notes on stoic thinking.",
        "Focus on control, discipline, and calm during stress.")
    add("Philosophy", "The Republic", "Plato", "9780140455113",
        "A dialogue about justice and society.",
        "Explores ideal leadership and the meaning of fairness.")
    add("Philosophy", "Beyond Good and Evil", "Friedrich Nietzsche", "9780140449235",
        "A critique of traditional morality.",
        "Challenges readers to question values and assumptions.")
    add("Philosophy", "The Art of War", "Sun Tzu", "9781599869773",
        "Classic strategy book with simple lessons.",
        "Planning and discipline are key ideas for victory and peace.")
    add("Philosophy", "Man's Search for Meaning", "Viktor E. Frankl", "9780807014271",
        "Finding meaning in suffering and hardship.",
        "Purpose can help people endure and rebuild their life.")
    add("Philosophy", "Thus Spoke Zarathustra (Selections)", "Friedrich Nietzsche", "9780140441185",
        "A philosophical novel about values and growth.",
        "Uses stories to explore personal transformation.")
    add("Philosophy", "The Problems of Philosophy", "Bertrand Russell", "9780192854230",
        "An introduction to philosophical thinking.",
        "Asks simple questions about knowledge and reality.")
    add("Philosophy", "The Stranger", "Albert Camus", "9780679720201",
        "A short novel about meaning and existence.",
        "A detached character faces consequences and absurdity.")
    add("Philosophy", "Sophie's World", "Jostein Gaarder", "9780374530716",
        "A story that teaches philosophy.",
        "A girl learns major philosophical ideas through mysterious letters.")
    add("Philosophy", "Letters from a Stoic", "Seneca", "9780140442106",
        "Stoic advice for daily life.",
        "Simple lessons on time, fear, and character.")
    add("Philosophy", "On the Shortness of Life", "Seneca", "9780140442441",
        "A short book about using time wisely.",
        "Encourages focus on meaningful work and values.")
    add("Philosophy", "Tao Te Ching (Selections)", "Lao Tzu", "9780061142666",
        "A classic on balance and simplicity.",
        "Promotes calm, humility, and natural flow in life.")

    # Fantasy
    add("Fantasy", "Harry Potter and the Sorcerer's Stone", "J. K. Rowling", "9780590353427",
        "A boy discovers he is a wizard and enters a magical school.",
        "Harry makes friends, faces mysteries, and learns bravery in his first year.")
    add("Fantasy", "The Fellowship of the Ring", "J. R. R. Tolkien", "9780261103573",
        "A group begins a dangerous quest to destroy a powerful ring.",
        "Frodo and allies leave safety behind to stop a growing darkness.")
    add("Fantasy", "A Game of Thrones", "George R. R. Martin", "9780553593716",
        "Noble families compete for power in a harsh world.",
        "Politics and loyalty collide while danger rises in the north.")
    add("Fantasy", "The Name of the Wind", "Patrick Rothfuss", "9780756404741",
        "A gifted young man tells his life story.",
        "Kvothe’s tale mixes talent, struggle, and mystery.")
    add("Fantasy", "Mistborn: The Final Empire", "Brandon Sanderson", "9780765311788",
        "A thief joins a rebellion with a unique magic system.",
        "Vin learns to trust and fight a ruler who seems unbeatable.")
    add("Fantasy", "The Lion, the Witch and the Wardrobe", "C. S. Lewis", "9780064471046",
        "Children enter a magical land through a wardrobe.",
        "They learn courage and sacrifice while helping a kingdom in winter.")
    add("Fantasy", "Eragon", "Christopher Paolini", "9780375826696",
        "A farm boy finds a dragon egg.",
        "Eragon becomes a rider and faces an evil empire.")
    add("Fantasy", "The Golden Compass", "Philip Pullman", "9780440418320",
        "A girl travels north to uncover a dangerous secret.",
        "Lyra’s courage grows as she faces powerful enemies.")
    add("Fantasy", "The Way of Kings", "Brandon Sanderson", "9780765326355",
        "Epic fantasy with war, honor, and discovery.",
        "Different characters’ paths connect to a bigger mystery.")
    add("Fantasy", "The Last Wish", "Andrzej Sapkowski", "9780316029186",
        "Short stories about a monster hunter.",
        "Geralt faces moral choices in a world of magic and danger.")
    add("Fantasy", "Percy Jackson: The Lightning Thief", "Rick Riordan", "9780786838658",
        "A boy discovers he is related to Greek gods.",
        "Percy goes on a quest to stop a war among gods.")
    add("Fantasy", "Stardust", "Neil Gaiman", "9780061142024",
        "A fairy tale adventure beyond a village wall.",
        "A young man searches for a fallen star and finds real love and courage.")

    # Geography
    add("Geography", "Prisoners of Geography", "Tim Marshall", "9781783962439",
        "How geography shapes politics and global power.",
        "Explains world events using maps, borders, and natural barriers in a simple way.")
    add("Geography", "The Power of Geography", "Tim Marshall", "9781783964877",
        "A follow-up look at key regions shaping the future.",
        "Shows how land, sea routes, and geography affect real political decisions.")
    add("Geography", "The Revenge of Geography", "Robert D. Kaplan", "9780812982220",
        "Geography as a strong force behind history and strategy.",
        "Uses places and patterns to explain why countries act the way they do.")
    add("Geography", "How to Lie with Maps", "Mark Monmonier", "9780226534213",
        "How maps can be misleading (sometimes on purpose).",
        "Teaches basic map reading and how to notice hidden bias.")
    add("Geography", "Longitude", "Dava Sobel", "9780802715296",
        "The story of solving the longitude problem at sea.",
        "A simple history of navigation and the invention that changed travel.")
    add("Geography", "The Map That Changed the World", "Simon Winchester", "9780061767906",
        "A mapmaker’s work that helped shape modern geology.",
        "A short history showing how mapping and science connected.")
    add("Geography", "The Geography of Bliss", "Eric Weiner", "9780446698894",
        "A travel-based search for happiness around the world.",
        "Uses countries and culture to discuss what makes people feel happy.")
    add("Geography", "National Geographic Atlas of the World", "National Geographic", "9781426219874",
        "A famous atlas with maps and world facts.",
        "A visual guide to countries, oceans, and major world regions.")
    add("Geography", "A Short History of the World", "Christopher Lascelles", "9781409350866",
        "World history connected with simple geography context.",
        "Links major events with places to make the timeline easier to understand.")
    add("Geography", "The Atlas of Middle-earth", "Karen Wynn Fonstad", "9780618126989",
        "Maps and geography of Tolkien’s world.",
        "Explains locations and journeys using clear maps and notes.")
    add("Geography", "The World: A Brief Introduction", "Richard Haass", "9780399562396",
        "A simple guide to today’s world and global issues.",
        "Explains key topics like power, trade, and conflicts in a readable style.")
    add("Geography", "Oxford School Atlas", "Oxford University Press", "9780199061594",
        "A school atlas used for learning map skills.",
        "Basic political and physical maps to support geography study.")

    # Space
    add("Space", "Astrophysics for People in a Hurry", "Neil deGrasse Tyson", "9780393609394",
        "Quick answers to big questions about the universe.",
        "Simple explanations of stars, galaxies, and space-time for beginners.")
    add("Space", "The Universe in a Nutshell", "Stephen Hawking", "9780553802023",
        "Modern physics explained with big ideas and visuals.",
        "Covers black holes, time, and the universe in a friendly overview.")
    add("Space", "Packing for Mars", "Mary Roach", "9780393358575",
        "Funny and factual look at space travel life.",
        "Explains what astronauts face, from training to everyday challenges.")
    add("Space", "The Right Stuff", "Tom Wolfe", "9780312427566",
        "The early days of America’s space program.",
        "Stories of test pilots and astronauts with real history and drama.")
    add("Space", "Apollo 13", "Jim Lovell & Jeffrey Kluger", "9780385487320",
        "A mission that turned into a survival story.",
        "Shows teamwork and problem-solving when everything went wrong.")
    add("Space", "Endurance", "Scott Kelly", "9781524731593",
        "A year in space and the life of an astronaut.",
        "Daily routines and challenges of living in space for long time.")
    add("Space", "The Planets", "Brian Cox", "9780008301481",
        "A modern guide to planets and space exploration.",
        "Explains planets with clear descriptions and interesting facts.")
    add("Space", "Black Holes and Time Warps", "Kip S. Thorne", "9780393312768",
        "A readable story of gravity and black holes.",
        "Explains big physics ideas through real discoveries and people.")
    add("Space", "Cosmos: Possible Worlds", "Ann Druyan", "9781426221778",
        "A modern journey through science and space.",
        "Explores future possibilities and how science changes our life.")
    add("Space", "A Man on the Moon", "Andrew Chaikin", "9780143112355",
        "The story of the Apollo missions.",
        "A clear history of moon landings with human moments.")
    add("Space", "Hidden Figures", "Margot Lee Shetterly", "9780062363596",
        "The women mathematicians behind early space missions.",
        "A true story of talent, barriers, and major space achievements.")
    add("Space", "Spaceflight", "Giles Sparrow", "9781465420962",
        "A visual introduction to rockets and missions.",
        "Covers key launches and simple concepts in an easy format.")

    # Textbooks
    add("Textbooks", "Concepts of Physics (Part 1)", "H. C. Verma", "9788177091878",
        "A popular physics book for students.",
        "Covers basics with clear concepts and practice problems.")
    add("Textbooks", "Campbell Biology", "Lisa A. Urry", "9780134093413",
        "A standard biology textbook used worldwide.",
        "Explains life science topics with diagrams and simple explanations.")
    add("Textbooks", "Calculus: Early Transcendentals", "James Stewart", "9781285741550",
        "A widely used calculus textbook.",
        "Covers limits, derivatives, and integrals with examples and exercises.")
    add("Textbooks", "Fundamentals of Physics", "Halliday, Resnick, Walker", "9781118230718",
        "A common university physics textbook.",
        "Explains mechanics, waves, and electricity with step-by-step problems.")
    add("Textbooks", "Organic Chemistry", "Paula Yurkanis Bruice", "9781118452288",
        "A student-friendly organic chemistry textbook.",
        "Introduces reactions and mechanisms with simple patterns and examples.")
    add("Textbooks", "University Physics with Modern Physics", "Young & Freedman", "9780321973610",
        "A complete physics course book for engineering/science.",
        "Covers core physics topics with worked examples.")
    add("Textbooks", "Engineering Mechanics: Statics", "R. C. Hibbeler", "9780133915426",
        "A standard textbook for engineering mechanics.",
        "Teaches forces, equilibrium, and structures using clear steps.")
    add("Textbooks", "Microeconomics", "Paul Krugman & Robin Wells", "9781319098780",
        "A clear textbook introduction to microeconomics.",
        "Explains demand, supply, markets, and basic economic decisions.")
    add("Textbooks", "Principles of Macroeconomics", "N. Gregory Mankiw", "9781305971493",
        "A popular macroeconomics textbook.",
        "Covers GDP, inflation, unemployment, and economic growth.")
    add("Textbooks", "Data Structures and Algorithms Made Easy", "Narasimha Karumanchi", "9788193245279",
        "A student-focused DSA practice book.",
        "Simple explanations and many interview-style questions.")
    add("Textbooks", "Discrete Mathematics and Its Applications", "Kenneth H. Rosen", "9780073383095",
        "A common discrete math textbook for CSE.",
        "Logic, sets, graphs, and counting explained for beginners.")
    add("Textbooks", "Artificial Intelligence: A Modern Approach", "Stuart Russell & Peter Norvig", "9780134610993",
        "A well-known AI textbook.",
        "Covers AI basics and key ideas in a structured student-friendly way.")

    # Psychology (2-3 books)
    add("Psychology", "Influence", "Robert B. Cialdini", "9780062937650",
        "A classic book on persuasion and human behavior.",
        "Explains common persuasion principles with simple examples from real life.")
    add("Psychology", "Emotional Intelligence", "Daniel Goleman", "9780553383713",
        "How emotions affect success and relationships.",
        "Shows why self-awareness and empathy matter as much as IQ.")
    add("Psychology", "Man's Search for Meaning", "Viktor E. Frankl", "9780807014271",
        "A powerful story about meaning and purpose in hard times.",
        "Explains how purpose can help people survive and rebuild their life.")

    # Productivity (2-3 books)
    add("Productivity", "Getting Things Done", "David Allen", "9780142000281",
        "A simple system to organize tasks and reduce stress.",
        "Focus on capturing tasks, clarifying next steps, and reviewing regularly.")
    add("Productivity", "Essentialism", "Greg McKeown", "9780804137386",
        "Do less but better by focusing on what matters.",
        "Helps remove distractions and choose the most important work.")
    add("Productivity", "The ONE Thing", "Gary Keller", "9781885167774",
        "A focus-based approach to productivity.",
        "Shows how one clear priority can improve results and time use.")

    # Finance (2-3 books)
    add("Finance", "Rich Dad Poor Dad", "Robert T. Kiyosaki", "9781612680194",
        "Basic money lessons explained through two mindsets.",
        "Teaches simple ideas about assets, liabilities, and financial habits.")
    add("Finance", "The Intelligent Investor", "Benjamin Graham", "9780060555665",
        "A classic on long-term value investing.",
        "Explains investing with safety, patience, and simple principles.")
    add("Finance", "The Psychology of Money", "Morgan Housel", "9780857197689",
        "How behavior affects money decisions.",
        "Shows simple lessons about patience, risk, and long-term thinking.")

    # Entrepreneurship (2-3 books)
    add("Entrepreneurship", "Zero to One", "Peter Thiel", "9780804139298",
        "How to build something new that creates value.",
        "Simple startup thinking about innovation, competition, and unique ideas.")
    add("Entrepreneurship", "The Lean Startup", "Eric Ries", "9780307887894",
        "Build products with feedback and fast learning.",
        "Explains MVP, testing, and improvement in a beginner-friendly way.")
    add("Entrepreneurship", "Start with Why", "Simon Sinek", "9781591846444",
        "Leaders inspire by explaining purpose first.",
        "Shows why clarity of purpose helps teams and businesses grow.")

    # Health (2-3 books)
    add("Health", "Why We Sleep", "Matthew Walker", "9781501144318",
        "A guide to the science of sleep and its benefits.",
        "Explains how sleep affects learning, health, mood, and performance.")
    add("Health", "How Not to Die", "Michael Greger", "9781250066114",
        "Lifestyle and food choices for better health.",
        "Simple health tips with evidence-based explanations.")
    add("Health", "The Body", "Bill Bryson", "9780385539300",
        "A fun tour of the human body.",
        "Explains how the body works with interesting facts and simple storytelling.")

    # Motivation (2-3 books)
    add("Motivation", "Drive", "Daniel H. Pink", "9781594484803",
        "What motivates people beyond money and rewards.",
        "Shows autonomy, mastery, and purpose as key motivation ideas.")
    add("Motivation", "Grit", "Angela Duckworth", "9781501111105",
        "Why perseverance matters more than talent.",
        "Explains how long-term effort shapes achievement in study and life.")
    add("Motivation", "Can't Hurt Me", "David Goggins", "9781544512280",
        "A story about mental toughness and self-discipline.",
        "Motivational lessons on pushing limits and staying consistent.")

    return data

