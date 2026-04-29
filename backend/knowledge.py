"""
Official Morgan State University CS curriculum knowledge base.
Source: Morgan State University 2022–2024 Undergraduate Catalog (Archived)
        catalog.morgan.edu — School of Computer, Mathematical, and Natural Sciences
All course numbers, titles, and credit hours are taken directly from that document.
"""

MORGAN_KNOWLEDGE = {

    "source": {
        "document": "Morgan State University 2022–2024 Undergraduate Catalog (Archived)",
        "url": "https://catalog.morgan.edu",
        "school": "School of Computer, Mathematical and Natural Sciences",
        "degree": "Computer Science, B.S.",
        "note": "All course data below comes directly from this official document."
    },

    "university": {
        "name": "Morgan State University",
        "nickname": "The Truth",
        "mascot": "Spike the Bear",
        "colors": "Blue and Gold",
        "location": "Baltimore, Maryland",
        "type": "HBCU — Historically Black College and University",
        "founded": 1867,
        "website": "https://www.morgan.edu",
        "phone": "443-885-3333"
    },

    "csProgram": {
        "department": "Department of Computer Science",
        "college": "School of Computer, Mathematical and Natural Sciences",
        "degrees": ["B.S. Computer Science", "M.S. Computer Science", "Ph.D. Computer Science"],
        "accreditation": "ABET Accredited",
        "advising_office": "SCMNS Advising Center",
        "advising_email": "scmns.advising@morgan.edu",
        "advising_location": "Carnegie Hall"
    },

    # ── Graduation Requirements (directly from the catalog) ──────────────────
    "graduationRequirements": {
        "total_credits": 120,
        "credit_breakdown": {
            "general_education_and_university": 44,
            "supporting_courses": 11,
            "required_cs_major_courses": 65
        },
        "school_wide_requirements": [
            "Complete all Computer Science Major Requirements",
            "Complete all General Education Requirements",
            "Earn 6 credits in the Complementary Studies Program (required for all SCMNS majors)",
            "Pass the Senior Departmental Comprehensive Examination",
            "Take all junior- and senior-level major requirements at Morgan State University (written Dean permission required to take elsewhere)",
            "Earn a cumulative GPA of 2.0 or better",
            "Earn a major GPA of 2.0 or better",
            "No outstanding grades below 'C' in any major or required supporting course"
        ]
    },

    # ── General Education & University Requirements (44 credits) ─────────────
    "generalEducationRequirements": {
        "total_credits": 44,
        "courses": [
            {"course": "ENGL 101 or ENGL 111", "title": "Freshman Composition I (or Honors)", "credits": 3, "area": "EC"},
            {"course": "ENGL 102 or ENGL 112", "title": "Freshman Composition II (or Honors)", "credits": 3, "area": "EC"},
            {"course": "MATH 241*",             "title": "Calculus I", "credits": 4, "area": "MQ"},
            {"course": "COSC 111*",             "title": "Introduction to Computer Science I", "credits": 4, "area": "IM"},
            {"course": "XXXX",                  "title": "HH General Education Requirement", "credits": 3, "area": "HH"},
            {"course": "XXXX",                  "title": "AH General Education Requirement", "credits": 3, "area": "AH"},
            {"course": "XXXX",                  "title": "AH General Education Requirement", "credits": 3, "area": "AH"},
            {"course": "XXXX",                  "title": "BP General Education Requirement (with lab)", "credits": 4, "area": "BP"},
            {"course": "XXXX",                  "title": "BP General Education Requirement (no lab)", "credits": 3, "area": "BP"},
            {"course": "XXXX",                  "title": "SB General Education Requirement", "credits": 3, "area": "SB"},
            {"course": "XXXX",                  "title": "SB General Education Requirement", "credits": 3, "area": "SB"},
            {"course": "XXXX",                  "title": "CI General Education Requirement", "credits": 3, "area": "CI"},
            {"course": "XXXX",                  "title": "CT General Education Requirement", "credits": 3, "area": "CT"},
            {"course": "ORNS 106",              "title": "Freshman Orientation for Majors in SCMNS", "credits": 1, "area": "orientation"},
            {"course": "XXXX",                  "title": "Physical Activity or FIN 101 or MIND 101 or DSVG 101 or FACS 102", "credits": 1, "area": "wellness"}
        ],
        "note": "* Denotes a course that may fulfill a Gen Ed requirement but must be completed with a grade of 'C' or higher."
    },

    # ── Supporting Courses (11 credits) ──────────────────────────────────────
    "supportingCourses": {
        "total_credits": 11,
        "courses": [
            {"course": "MATH 241*", "title": "Calculus I",                         "credits": 4},
            {"course": "MATH 242",  "title": "Calculus II",                        "credits": 4},
            {"course": "MATH 312",  "title": "Linear Algebra I",                   "credits": 3},
            {"course": "MATH 331",  "title": "Applied Probability and Statistics", "credits": 3},
            {"course": "COSC 201",  "title": "Computer Ethics",                    "credits": 1}
        ],
        "note": "MATH 241 must be completed with a grade of 'C' or higher. Credits are shared with Gen Ed requirements."
    },

    # ── Required CS Major Courses (65 credits) ───────────────────────────────
    "requiredCSCourses": {
        "total_credits": 65,
        "grade_requirement": "All courses must be completed with a grade of 'C' or higher.",
        "core_courses": [
            {"course": "COSC 111*", "title": "Introduction to Computer Science I",     "credits": 4},
            {"course": "COSC 112",  "title": "Introduction to Computer Science II",    "credits": 4},
            {"course": "COSC 220",  "title": "Data Structures and Algorithms",         "credits": 4},
            {"course": "COSC 241",  "title": "Computer Systems and Digital Logic",     "credits": 3},
            {"course": "COSC 281",  "title": "Discrete Structure",                     "credits": 3},
            {"course": "COSC 349",  "title": "Computer Networks",                      "credits": 3},
            {"course": "COSC 351",  "title": "Cybersecurity",                          "credits": 3},
            {"course": "COSC 352",  "title": "Organization of Programming Languages",  "credits": 3},
            {"course": "COSC 354",  "title": "Operating Systems",                      "credits": 3},
            {"course": "COSC 458",  "title": "Software Engineering",                   "credits": 3},
            {"course": "COSC 459",  "title": "Database Design",                        "credits": 3},
            {"course": "COSC 490",  "title": "Senior Project",                         "credits": 3}
        ],
        "electives": {
            "group_a": {
                "description": "Choose three (3) courses",
                "courses": [
                    {"course": "COSC 238", "title": "Object Oriented Programming",     "credits": 4},
                    {"course": "COSC 239", "title": "Java Programming",                "credits": 3},
                    {"course": "COSC 243", "title": "Computer Architecture",           "credits": 3},
                    {"course": "COSC 251", "title": "Introduction to Data Science",    "credits": 3},
                    {"course": "CLCO 261", "title": "Introduction to Cloud Computing", "credits": 3}
                ]
            },
            "group_b": {
                "description": "Choose two (2) courses",
                "courses": [
                    {"course": "COSC 320", "title": "Algorithm Design and Analysis",               "credits": 3},
                    {"course": "COSC 323", "title": "Introduction to Cryptography",                "credits": 3},
                    {"course": "COSC 332", "title": "Introduction to Game Design and Development", "credits": 3},
                    {"course": "COSC 338", "title": "Mobile App Design & Development",             "credits": 3},
                    {"course": "COSC 383", "title": "Numerical Methods and Programming",           "credits": 3},
                    {"course": "COSC 385", "title": "Theory of Languages and Automata",            "credits": 3},
                    {"course": "COSC 386", "title": "Introduction to Quantum Computing",           "credits": 3},
                    {"course": "MATH 313", "title": "Linear Algebra II",                           "credits": 3},
                    {"course": "EEGR 317", "title": "Electronic Circuits",                         "credits": 4}
                ]
            },
            "group_c": {
                "description": "Choose four (4) courses",
                "courses": [
                    {"course": "COSC 470 or COSC 472", "title": "Artificial Intelligence or Introduction to Machine Learning", "credits": 3},
                    {"course": "COSC 460", "title": "Computer Graphics",                                   "credits": 3},
                    {"course": "COSC 480", "title": "Introduction to Image Processing and Analysis",       "credits": 3},
                    {"course": "COSC 486", "title": "Applied Quantum Computing",                           "credits": 3},
                    {"course": "COSC 491", "title": "Conference Course",                                   "credits": 3},
                    {"course": "COSC 498", "title": "Senior Internship",                                   "credits": 3},
                    {"course": "COSC 499", "title": "Senior Research or Teaching/Tutorial Assistantship", "credits": 3},
                    {"course": "CLCO 471", "title": "Data Analytics in Cloud",                             "credits": 3}
                ]
            },
            "group_d": {
                "description": "Choose one (1) course",
                "courses": [
                    {"course": "INSS 391", "title": "IT Infrastructure and Security",          "credits": 3},
                    {"course": "INSS 494", "title": "Information Security and Risk Management","credits": 3},
                    {"course": "EEGR 481", "title": "Introduction to Network Security",        "credits": 3},
                    {"course": "EEGR 483", "title": "Introduction to Security Management",     "credits": 3},
                    {"course": "XXXX",     "title": "Any 300-400 level COSC course not previously taken", "credits": 3}
                ]
            }
        }
    },

    # ── Year-by-year guide (based on official course sequence) ───────────────
    "yearGuide": {
        "freshman": {
            "credits": "0-29",
            "focus": "General Education foundations and intro CS courses",
            "typical_courses": [
                "ORNS 106 — Freshman Orientation for SCMNS Majors (1 cr)",
                "COSC 111 — Introduction to Computer Science I (4 cr)",
                "COSC 112 — Introduction to Computer Science II (4 cr)",
                "ENGL 101/111 — Freshman Composition I (3 cr)",
                "ENGL 102/112 — Freshman Composition II (3 cr)",
                "MATH 241 — Calculus I (4 cr)",
                "General Education requirements (HH, AH, SB, CI, CT, BP, wellness)"
            ],
            "grade_note": "COSC 111 and MATH 241 require a 'C' or higher to progress."
        },
        "sophomore": {
            "credits": "30-59",
            "focus": "Core CS courses and supporting math",
            "typical_courses": [
                "COSC 220 — Data Structures and Algorithms (4 cr)",
                "COSC 241 — Computer Systems and Digital Logic (3 cr)",
                "COSC 281 — Discrete Structure (3 cr)",
                "MATH 242 — Calculus II (4 cr)",
                "MATH 312 — Linear Algebra I (3 cr)",
                "COSC 201 — Computer Ethics (1 cr)",
                "Remaining General Education requirements"
            ],
            "grade_note": "All CS major courses require a 'C' or higher."
        },
        "junior": {
            "credits": "60-89",
            "focus": "Upper-level required CS courses and electives",
            "typical_courses": [
                "COSC 349 — Computer Networks (3 cr)",
                "COSC 351 — Cybersecurity (3 cr)",
                "COSC 352 — Organization of Programming Languages (3 cr)",
                "COSC 354 — Operating Systems (3 cr)",
                "COSC 458 — Software Engineering (3 cr)",
                "COSC 459 — Database Design (3 cr)",
                "MATH 331 — Applied Probability and Statistics (3 cr)",
                "Group A and Group B electives"
            ],
            "grade_note": "All junior-level major requirements must be taken at Morgan State unless the Dean grants written permission."
        },
        "senior": {
            "credits": "90+",
            "focus": "Senior Project, remaining electives, and graduation preparation",
            "typical_courses": [
                "COSC 490 — Senior Project (3 cr)",
                "Group C electives — choose 4 courses",
                "Group D elective — choose 1 course",
                "Any remaining degree requirements"
            ],
            "requirements": [
                "Pass the Senior Departmental Comprehensive Examination",
                "Apply for graduation the semester BEFORE your final semester — contact the Registrar",
                "Confirm your degree audit with your advisor at scmns.advising@morgan.edu",
                "All senior-level major requirements must be completed at Morgan State unless the Dean grants prior written permission"
            ]
        }
    },

    # ── Official campus resources (verified morgan.edu contacts) ─────────────
    "resources": {
        "advising": {
            "name": "SCMNS Advising Center",
            "email": "scmns.advising@morgan.edu",
            "location": "Carnegie Hall",
            "url": "https://www.morgan.edu/scmns"
        },
        "registrar": {
            "name": "Office of the Registrar",
            "url": "https://www.morgan.edu/registrar",
            "note": "For graduation application, degree audit, and transcript requests."
        },
        "financialAid": {
            "name": "Office of Student Financial Aid",
            "location": "Truth Hall",
            "phone": "443-885-3170",
            "url": "https://www.morgan.edu/financial_aid"
        },
        "tutoring": {
            "name": "Student Success Center",
            "location": "Montebello Complex",
            "url": "https://www.morgan.edu/student_success_center"
        },
        "career": {
            "name": "Career Center",
            "location": "Montebello D Building",
            "url": "https://www.morgan.edu/career_center"
        },
        "mentalHealth": {
            "name": "Counseling Center",
            "location": "Montebello Complex C",
            "phone": "443-885-3130",
            "url": "https://www.morgan.edu/counseling_center"
        },
        "library": {
            "name": "Earl S. Richardson Library",
            "url": "https://www.morgan.edu/library"
        },
        "accessibility": {
            "name": "Office of Accessibility Services",
            "location": "Montebello Complex C",
            "url": "https://www.morgan.edu/accessibility"
        }
    },

    "clubs": [
        "CS Student Association (CSSA)",
        "National Society of Black Engineers (NSBE) — Morgan Chapter",
        "Association of Computing Machinery (ACM)",
        "Women in Computer Science",
        "Cybersecurity Club",
        "Game Development Club",
        "Data Science Club",
        "Robotics Team"
    ],

    # ── Faculty & Staff Directory ─────────────────────────────────────────────
    # Source: morgan.edu/computer-science/faculty-and-staff
    "facultyAndStaff": {
        "source": "Morgan State University — Department of Computer Science | morgan.edu/computer-science/faculty-and-staff",
        "address": "1700 East Cold Spring Lane, Baltimore, Maryland 21251",
        "department_phone": "(443) 885-3333",
        "social_media": "@Morgan_CompSci on Twitter / X",

        "departmentLeadership": [
            {
                "name": 'Shuangbao "Paul" Wang',
                "title": "Professor and Chair",
                "office": "McMechen Hall 507",
                "phone": "(443) 885-4503",
                "email": "shuangbao.wang@morgan.edu",
                "dept_email": "cs-chair@morgan.edu"
            },
            {
                "name": "Md Rahman",
                "title": "Professor, Associate Chair, Director of PhD Advanced Computing",
                "office": "McMechen Hall 629",
                "phone": "(443) 885-1056",
                "email": "Md.Rahman@morgan.edu"
            },
            {
                "name": "Radhouane Chouchane (Radwan Shushane)",
                "title": "Associate Professor, Director of Undergraduate Studies",
                "office": "McMechen Hall 624",
                "phone": "(443) 885-3745",
                "email": "Radwan.Shushane@morgan.edu"
            }
        ],

        "professors": [
            {
                "name": "Amjad Ali",
                "title": "Professor",
                "office": "McMechen Hall 502",
                "email": "amjad.ali@morgan.edu"
            },
            {
                "name": "Radhouane Chouchane (Radwan Shushane)",
                "title": "Associate Professor, Director of Undergraduate Studies",
                "office": "McMechen Hall 624",
                "phone": "(443) 885-3745",
                "email": "Radwan.Shushane@morgan.edu"
            },
            {
                "name": "Monireh Dabaghchian",
                "title": "Associate Professor",
                "office": "McMechen Hall 508",
                "phone": "(443) 885-2348",
                "email": "Monireh.Dabaghchian@morgan.edu"
            },
            {
                "name": "Jamell Dacon",
                "title": "Assistant Professor",
                "office": "McMechen Hall 625",
                "email": "jamell.dacon@morgan.edu"
            },
            {
                "name": "Jin Guo",
                "title": "Professor of Practice",
                "office": "McMechen Hall 502",
                "email": "jin.guo@morgan.edu"
            },
            {
                "name": "Vahid Heydari",
                "title": "Associate Professor",
                "office": "McMechen Hall 619",
                "email": "vahid.heydari@morgan.edu"
            },
            {
                "name": "Naja Mack",
                "title": "Assistant Professor",
                "office": "McMechen Hall 623",
                "lab": "McMechen Hall 616",
                "phone": "(443) 885-2402",
                "email": "Naja.Mack@morgan.edu"
            },
            {
                "name": "Jianzhou Mao",
                "title": "Research Assistant Professor",
                "office": "McMechen Hall 627",
                "email": "jianzhou.mao@morgan.edu"
            },
            {
                "name": "Blessing Ojeme",
                "title": "Assistant Professor",
                "office": "McMechen Hall 621",
                "email": "blessing.ojeme@morgan.edu"
            },
            {
                "name": "Roshan Paudel",
                "title": "Coordinator of the MS in Bioinformatics Program, Professor of Practice",
                "office": "McMechen Hall 507D",
                "phone": "(443) 885-3096",
                "email": "Roshan.Paudel@morgan.edu"
            },
            {
                "name": "Md Rahman",
                "title": "Professor, Associate Chair, Director of PhD Advanced Computing",
                "office": "McMechen Hall 629",
                "phone": "(443) 885-1056",
                "email": "Md.Rahman@morgan.edu"
            },
            {
                "name": "Eric Sakk",
                "title": "Associate Professor",
                "office": "McMechen Hall 507F",
                "phone": "(443) 885-3270",
                "email": "Eric.Sakk@morgan.edu"
            },
            {
                "name": "Vojislav Stojkovic",
                "title": "Associate Professor",
                "office": "McMechen Hall 507E",
                "phone": "(443) 885-1054",
                "email": "Vojislav.Stojkovic@morgan.edu"
            },
            {
                "name": "Timothy Oladunni",
                "title": "Assistant Professor",
                "office": "McMechen Hall 617",
                "email": "Timothy.Oladunni@morgan.edu"
            },
            {
                "name": 'Shuangbao "Paul" Wang',
                "title": "Professor and Chair",
                "office": "McMechen Hall 507",
                "phone": "(443) 885-4503",
                "email": "shuangbao.wang@morgan.edu"
            },
            {
                "name": "Guobin Xu",
                "title": "Associate Professor, Director of MS Advanced Computing",
                "office": "McMechen Hall 615",
                "email": "guobin.xu@morgan.edu"
            }
        ],

        "lecturers": [
            {
                "name": "Grace Steele",
                "title": "Lecturer",
                "office": "McMechen Hall 507C",
                "phone": "(443) 885-1053",
                "email": "Grace.Steele@morgan.edu"
            },
            {
                "name": "Dr. Sam Tannouri",
                "title": "Lecturer",
                "office": "McMechen Hall 628",
                "phone": "(443) 885-1055",
                "email": "Sam.Tannouri@morgan.edu"
            }
        ],

        "engineersInResidence": [
            {
                "name": "Rahmel Bailey",
                "title": "Engineer in Residence",
                "office": "McMechen Hall 618",
                "email": "rahmel.bailey@codepath.org"
            }
        ],

        "staff": [
            {
                "name": "Wendy Smith",
                "title": "Administrative Assistant",
                "office": "McMechen Hall 507A",
                "phone": "(443) 885-3962",
                "email": "Wendy.Smith@morgan.edu",
                "dept_email": "compsci@morgan.edu"
            }
        ],

        "departmentContacts": {
            "chair": {
                "person": 'Dr. Shuangbao "Paul" Wang',
                "location": "McMechen Hall Suite 507",
                "phone": "(443) 885-4503",
                "fax": "(443) 885-8213",
                "email": "cs-chair@morgan.edu"
            },
            "general_inquiries": {
                "person": "Ms. Wendy Smith (Administrative Assistant)",
                "location": "McMechen Hall Suite 507",
                "phone": "(443) 885-3962",
                "fax": "(443) 885-8213",
                "email": "compsci@morgan.edu"
            },
            "undergraduate_studies_director": {
                "person": "Radhouane Chouchane (Radwan Shushane)",
                "location": "McMechen Hall 624",
                "phone": "(443) 885-3745",
                "email": "Radwan.Shushane@morgan.edu"
            }
        }
    },

    "keyPolicies": {
        "minimum_grade": "A grade of 'C' or higher is required in all CS major courses and required supporting courses.",
        "cumulative_gpa": "A cumulative GPA of 2.0 or better is required for graduation.",
        "major_gpa": "A major GPA of 2.0 or better is required for graduation.",
        "senior_exam": "Students must pass the Senior Departmental Comprehensive Examination to graduate.",
        "residency": "All junior- and senior-level major requirements must be completed at Morgan State University unless the Dean grants prior written permission.",
        "graduation_application": "Apply for graduation in the semester BEFORE your final semester. Contact the Registrar at morgan.edu/registrar.",
        "add_drop": "The add/drop period is the first week of classes each semester. Check the academic calendar at morgan.edu.",
        "fafsa": "FAFSA opens October 1. Apply early for maximum aid. Contact Financial Aid at 443-885-3170."
    }
}
