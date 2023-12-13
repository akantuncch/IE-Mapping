# Resources documentation below

"""
Educational Resources:
- Workshops: These include various workshops aimed at skill development, such as Design Thinking workshops.
- Courses and Curriculum: Academic courses and curricula tailored to entrepreneurial and innovation skills, like Startup UNC, MS MedTech.
- Degree Programs: Specialized degree programs, for instance, dual degree programs in healthcare.
- Certificate Programs: Certification programs offering focused learning, such as a Certificate in Entrepreneurship & Strategy.
- Entrepreneurship Minor: Minor degree programs focused on entrepreneurship, e.g., the Shuford Program in Entrepreneurship.
- Events: Conferences and networking sessions that provide opportunities for learning, networking, and collaboration, like annual innovation symposiums or entrepreneur meetups.


Funding and Grants:
- Venture Funds: Funds specifically allocated for student ventures, like the 1789 Student Venture Fund.
- Grant Programs: Financial grant programs for innovation, such as the Eshelman Innovation Institute funding.
- Investment Networks: Networks facilitating investments, for example, the Carolina Angel Network.

Mentorship and Support:
- Mentorship Programs: Programs providing guidance and advice, like the Venture Catalyst Program.
- Entrepreneurs in Residence: Experienced entrepreneurs offering mentorship and support.
- Legal Support: Legal assistance services, such as those provided by Law School Pro Bono initiatives.
- Commercialization and Startup Support: Services aiding in commercializing innovations and supporting startups, including the Office of Technology Commercialization and KickStart Venture Services.

Research and Development Support:
- Research Grants: Funding opportunities for research initiatives, e.g., the Gillings Innovation Lab.
- Translational Research Support: Support for translating research into practical applications, such as FastTraCS and AdvanTx.
- Innovation Labs: Facilities and environments promoting innovation, like The Cube.
- Patent and Market Research: Services providing patent filing assistance and market research, exemplified by the Patent Landscape OTC.

Networking and Collaboration:
- Innovation Hubs and Districts: Spaces fostering innovation, such as downtown innovation districts.
- Innovation Networks: Networks established to promote collaboration and innovation, like the Innovate Carolina global Network.
- Collaborative Spaces: Physical or virtual spaces designed to encourage collaboration, for instance, the Innovation Space @ Franklin St.

Technology and Infrastructure:
- Maker Spaces: Facilities equipped with tools and technology for creating and prototyping, such as BeAM.
- Design Services: Services providing design and prototype development support, like ChAI Core.
- Accelerator Spaces: Spaces designed to accelerate the growth of startups, for example, the KickStart Accelerator.

Impact Measurement and Reporting:
- Data Management and Reporting Services: Services specializing in managing and reporting impact data, like Impact Measurement and Reporting Services.
- Economic and Social Impact Tracking: Tools and services for tracking the economic and social impact of innovation initiatives, exemplified by the Innovate Carolina Startups Database.

Discovery and Ideation Support:
- Customer Discovery and Market Opportunity Programs: Programs designed to identify customer needs and market opportunities, such as I-Corps.
- Needs Discovery Programs: Initiatives for identifying and understanding market and user needs, like ChAI Core and FastTraCS.
"""

nodes = [
    {
        "id": 1,
        "name": "Innovate Carolina",
        "techtype": ["General"],
        "description": "Works with a network of campus and community partners to connect innovators and entrepreneurs to a set of tools and resources to support their ideas, initiatives and ventures. Uses the network of resources and tools to help support fellows and faculty.",
        "resources": {
            "Impact Measurement and Reporting": [
                {
                    "type": "Data Management and Reporting Services",
                    "details": "Services specializing in managing and reporting impact data, like Impact Measurement and Reporting Services.",
                },
                {
                    "type": "Economic and Social Impact Tracking",
                    "details": "Tools and services for tracking the economic and social impact of innovation initiatives, exemplified by the Innovate Carolina Startups Database.",
                },
            ]
        },
        "affiliation": [
            "Office of Technology Commercialization",
            "KickStart Venture Services",
        ],
        "website": "https://innovate.unc.edu/",
    },
    {
        "id": 2,
        "name": "FastTraCS",
        "techtype": ["Medtech"],
        "description": "Designed for healthcare practitioners, researchers, and administrators seeking to identify opportunities to create MedTech solutions.",
        "resources": {
            "Discovery and Ideation Support": [
                {
                    "type": "Needs Discovery Programs",
                    "details": "Initiatives for identifying and understanding market and user needs.",
                }
            ],
            "Technology and Infrastructure": [
                {
                    "type": "Design Services",
                    "details": "Services providing design and prototype development support, like ChAI Core.",
                }
            ],
        },
        "affiliation": ["NC TraCS Institute", "School of Medicine"],
        "website": "https://tracs.unc.edu/index.php/services/fasttracs",
    },
    {
        "id": 3,
        "name": "The Eshelman Institute",
        "techtype": ["Therapeutics", "Digital Health"],
        "description": "Designed to fund translational research related to therapeutics focused on oncology, infectious disease, and neuroscience (including rare diseases). However, the Institute welcomes ideas for devices and diagnostics, and other therapeutic areas and services.",
        "resources": {
            "Funding and Grants": [
                {
                    "type": "Grant Programs",
                    "details": "Financial grant programs for innovation.",
                }
            ],
            "Mentorship and Support": [
                {
                    "type": "Entrepreneurs in Residence",
                    "details": "Experienced entrepreneurs offering mentorship and support.",
                },
                {
                    "type": "Commercialization and Startup Support",
                    "details": "Services aiding in commercializing innovations and supporting startups.",
                },
            ],
        },
        "affiliation": ["Eshelman School of Pharmacy"],
        "website": "https://unceii.org/",
    },
    {
        "id": 4,
        "name": "Venture Catalyst Program",
        "techtype": ["General"],
        "description": "This program provides startups with business support and entrepreneurial fellows with direct experiences translating scientific, technological and social-driven ideas into the market. Program matches each startup with entrepreneurial mentors and venture catalyst fellows. A year program as a cohort to meet with mentors as a fellow.",
        "resources": {
            "Funding and Grants": [
                {
                    "type": "Grant Programs",
                    "details": "Financial grant programs for innovation.",
                }
            ],
            "Mentorship and Support": [
                {
                    "type": "Mentorship Programs",
                    "details": "Programs providing guidance and advice.",
                }
            ],
        },
        "affiliation": ["KickStart Venture Services", "Innovate Carolina"],
        "website": "https://innovate.unc.edu/venture-catalyst-program/",
    },
    {
        "id": 5,
        "name": "Center for the Business of Health",
        "techtype": ["General"],
        "description": "The Center for the Business of Health brings together expertise from across the university to generate knowledge, prepare business leaders, and facilitate important discussions about healthcare's business aspects. It offers various programs and activities, including courses, research, events, and an advisory board, focusing on the intersection of business and health. The Center aims to explore and address contemporary challenges in the healthcare industry through education, research, and community engagement.",
        "resources": {
            "Educational Resources": [
                {
                    "type": "Events",
                    "details": {
                        "name": "Business of Healthcare Conference",
                        "description": "The annual Business of Healthcare Conference is hosted by Kenan-Flagler on campus each fall. Coordinated and led by the Healthcare Club, the conference attracts more than 400 attendees and features expert panels and keynote speakers discussing the most central healthcare issues facing our community. Healthcare club members have the unique opportunity to help plan, organize, and implement this event, which over the past few years has become one of the most well-attended and popular annual events at Kenan-Flagler.",
                    },
                }
            ]
        },
        "affiliation": ["Kenan-Flagler Business School"],
        "website": "https://cboh.unc.edu/",
    },
    {
        "id": 6,
        "name": "KickStart Venture Services",
        "techtype": ["General"],
        "description": "Supports research-based startup formation and growth by providing education, early-stage funding, and on-campus accelerator space particularly through the KickStart Commercialization Grant Awards. KickStart also connects founders to key service providers, management, and investors in the local innovation ecosystem.",
        "resources": {
            "Funding and Grants": [
                {
                    "type": "Grant Programs",
                    "details": "Financial grant programs for innovation.",
                }
            ],
            "Mentorship and Support": [
                {
                    "type": "Mentorship Programs",
                    "details": "Programs providing guidance and advice.",
                }
            ],
            "Technology and Infrastructure": [
                {
                    "type": "Accelerator Spaces",
                    "details": "Spaces designed to accelerate the growth of startups.",
                }
            ],
        },
        "affiliation": [
            "Office of Technology Commercialization",
            "Innovate Carolina",
        ],
        "website": "https://innovate.unc.edu/startup-accelerators-and-venture-services/kickstart-venture-services/",
    },
    {
        "id": 7,
        "name": "Office of Technology Commercialization",
        "techtype": ["General"],
        "description": "The Office of Technology Commercialization (OTC) focuses on accelerating the translation of ideas into meaningful products and services. It supports inventors, startups, and industry partners, offering guidance on bringing inventions to market, securing translational research funding, and managing Material Transfer Agreements (MTAs) and Confidential Disclosure Agreements (CDAs). The OTC also showcases the impact of commercialization through various reports and news, and it promotes innovation that benefits North Carolina, the world, and the university. ",
        "resources": {
            "Research and Development Support": [
                {
                    "type": "Patent and Market Research",
                    "details": "Services providing patent filing assistance and market research.",
                }
            ]
        },
        "affiliation": [
            "Innovate Carolina",
            "KickStart Venture Services",
        ],
        "website": "https://innovate.unc.edu/",
    },
]

"""
"Feeds Into" instead of "Flows to" – It implies a progression or development from one program to another.
"Originates From" instead of "Flows from" – This highlights the source or foundational aspect of one program leading to another.
"Umbrella Program" instead of "Parent Program" – It conveys the idea of a broader, encompassing program that oversees or encompasses smaller initiatives.
"Sub-Program" instead of "Child Program" – This term suggests a smaller, more focused initiative under the larger program.
"Partners With" instead of "Collaborates With" – This could imply a more formal or structured relationship between programs.
"""

edges = [
    {"from": 1, "to": 6, "relationship": "Umbrella Program"},
    {"from": 1, "to": 7, "relationship": "Umbrella Program"},
    {"from": 2, "to": 6, "relationship": "Feeds Into"},
    {"from": 2, "to": 7, "relationship": "Feeds Into"},
    {"from": 3, "to": 6, "relationship": "Feeds Into"},
    {"from": 3, "to": 7, "relationship": "Feeds Into"},
    {"from": 4, "to": 6, "relationship": "Sub-Program"},
    {"from": 5, "to": 1, "relationship": "Partners With"},
    {"from": 5, "to": 3, "relationship": "Partners With"},
    {"from": 6, "to": 7, "relationship": "Flows From"},
    {"from": 6, "to": 1, "relationship": "Sub-Program"},
    {"from": 7, "to": 6, "relationship": "Feeds Into"},
    {"from": 7, "to": 1, "relationship": "Sub-Program"},
    {"from": 7, "to": 2, "relationship": "Flows From"},
    {"from": 7, "to": 3, "relationship": "Flows From"},
]
