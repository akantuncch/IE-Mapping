""" Schema for Stage

Idea:
Description: The initial stage where the basic idea is formed.
Characteristics: High level of uncertainty; needs conceptual validation.

Need Validation:
Description: Validating the market and user need for the idea.
Characteristics: Involves market research, potential customer interviews.

Concept Generation:
Description: Developing a more concrete concept based on validated needs.
Characteristics: Early design and feasibility studies; conceptual modeling.

Development:
Description: Turning the concept into a tangible prototype or product.
Characteristics: Involves design refinement, prototype development, initial testing.

Preclinical Testing:
Description: Testing the prototype in a controlled, non-human environment.
Characteristics: Safety and efficacy tests; may involve lab testing or simulations.

Clinical Testing:
Description: Testing the product in a clinical setting with human subjects.
Characteristics: Clinical trials; involves regulatory considerations, human safety and effectiveness.

Market Ready:
Description: Product is fully developed, tested, and ready for market launch.
Characteristics: Has passed all necessary regulatory approvals; ready for commercialization.
 """

# Schema for readiness_level
""" Conceptual (Level 1):

Description: Initial concept with basic idea outlined.
Characteristics: No prototype or proof of concept yet.
Research (Level 2):

Description: Basic research completed to validate the concept.
Characteristics: Preliminary studies or theoretical validation in place.
Experimental Proof (Level 3):

Description: Early-stage experimental evidence supporting the concept.
Characteristics: Lab testing or initial prototypes demonstrating basic functionality.
Prototype Development (Level 4):

Description: Functional prototype developed.
Characteristics: Prototype demonstrates key features but is not yet ready for real-world testing.
Validation in Controlled Environment (Level 5):

Description: Technology validated in a controlled or laboratory setting.
Characteristics: Shows potential for practical application; may need further development for real-world conditions.
Pilot Testing (Level 6):

Description: Undergoing pilot testing in an operational environment.
Characteristics: Tested in conditions that closely simulate real-world application.
Advanced Prototype (Level 7):

Description: Advanced prototype suitable for demonstrations and further testing.
Characteristics: Near-final design; testing for reliability and usability.
Pre-Commercial (Level 8):

Description: Ready for final refinements before commercial release.
Characteristics: Proven in test environments; final adjustments for market readiness underway.
Market Ready (Level 9):

Description: Fully developed and ready for commercial deployment.
Characteristics: Meets all regulatory requirements and is ready for mass production and market entry.

 """
tech_data = [
    {
        "id": "T1",
        "name": "Pelvic Floor Physical Therapy Smart Wand",
        "techtype": "Medtech",
        "short_description": "An innovative three-part physical therapy system and device for pelvic floor dysfunction (PFD), featuring a sensor-integrated vaginal smart wand and an integrated app for biofeedback.",
        "long_description": "Pelvic floor dysfunction (PFD) occurs when the pelvic floor muscles become too tight and/or too weak resulting in a failure to function properly. PFD can result in a wide range of genitourinary complaints for both men and women including discomfort, lower urinary tract symptoms, defecatory dysfunction, and sexual pain. Pelvic floor physical therapy (PFPT) is a first-line treatment for high tone pelvic floor dysfunction and other pelvic floor dysfunction disorders. This therapy is typically done by in person therapy one to two times per week for 8-12 weeks. Consequently, this is associated with numerous burdens to therapy including financial and time limitations, perceived lack of utility and fear of intimacy of the internal treatment. PFPT is often achieved using static dilator devices, which do not provide any user feedback and can therefore be ineffective and/or potentially harmful when used improperly, especially by patients in self-therapy. Researchers at UNC have developed a three-part integrated system for guided pelvic floor physical therapy which features a sensor integrated PFPT smart therapy wand, a charging station, and a smartphone app that provides critical biofeedback to safely administer and maximize the benefits of PFPT. The smart wand is mapped to the pelvic floor muscles to guide targeted massage and pressure to release tension associated with PFD. This three-part system consists of a smart therapy wand, a charging station, and an integrated app which displays the pelvic floor muscles and highlights which sets of muscles are being treated. This smart wand features multiple sensors which collect the position of the PF therapy device in respect to key pelvic floor muscles. These sensors transmit key biofeedback to an app where the user can measure contractile strength with a kegel, assess the ability of the pelvic floor to relax, and assist the user in directing the inserted wand for maximal therapy efficacy. Further this system can be integrated with existing electronic medical records for use by providers for prescribing therapy regimens and sending notifications to patients to complete exercises. This unique combination of features enables effective at home and in-office PFPT. Benefits Three- part system enables real-time user feedback to allow for safe and effective at home PFPT Smart wand features multiple sensors that provide positional feedback and other key measurements for PFPT Multiple smart wand designs and configurations allow for use across multiple patient populations The system is designed for integration with electronic medical records enabling health care providers to monitor and prescribe the desired therapy regimen.",
        "stage": "Development",
        "readiness_level": "Prototype",
        "expertise_required": "Medtech",
        "resource_needs": {
            "Research and Development Support": [
                "Patent and Market Research",
                "Research Grants",
            ],
            "Technology and Infrastructure": ["Design Services"],
            "Mentorship and Support": ["Commercialization and Startup Support"],
        },
        "readiness_level": "Research",
        "inventor": {
            "name": "Erin Carey",
            "department": "Department of Obstetrics and Gynecology",
            "school": "School of Medicine",
            "role": "Faculty",
        },
    },
    {
        "id": "T2",
        "name": "ENVIROSCAN",
        "techtype": "Tech",
        "short_description": "A web-based platform for monitoring and analyzing environmental data, including air and water quality, soil quality, and biodiversity.",
        "long_description": "EnviroScan is an innovative web-based platform that allows users to access real-time and historical data on various environmental indicators such as air quality, water quality, soil quality, climate change, and biodiversity. The platform provides tools for visualizing this data through interactive maps, charts, and dashboards, enabling users to compare different regions and indicators. One of its key features is the ability to view environmental contaminants, sociodemographic information, environmental justice indicators, and health outcomes both individually and in various combinations, offering a comprehensive perspective on environmental issues. EnviroScan is designed to cater to the needs of the public, policymakers, and stakeholders, promoting awareness and action on environmental issues. Additionally, the platform supports the integration of private data for in-depth analysis while ensuring its segregation from publicly available data.",
        "stage": "Market-Ready",
        "readiness_level": "Pre-Commercial",
        "expertise_required": "Environmental Science",
        "resource_needs": {
            "Mentorship and Support": ["Commercialization and Startup Support"],
        },
        "inventor": {
            "name": "Dr. Jane Doe",
            "department": "Department of Environmental Science",
            "school": "Gillings School of Public Health",
            "role": "Faculty",
        },
    },
    {
        "id": "T3",
        "name": "STING-IL-35 Axis Targeting Treatment for Cold Tumors",
        "techtype": "Therapeutics",
        "short_description": "A novel dual treatment targeting the STING-IL-35 axis to enhance the innate immune response and treat immunosuppressive 'cold' tumors.",
        "long_description": "Tumors known as 'cold' are characterized by an immunosuppressive environment, making them resistant to immunotherapy. One such example is pancreatic ductal adenocarcinoma (PDAC). Researchers at UNC have developed a new method combining a STING agonist with an IL-35 antagonist, effectively reducing cancer immunosuppression. This method was tested in cell-based and orthotopic PDAC mouse studies, showing that it potentiates NK cell efficiency and drives key pathways for productive NK cellular proliferation and effector functions, enhancing anti-tumor activity. This approach aims to overcome the limitations of current STING-agonist therapies by targeting the STING-IL-35 axis, offering a new avenue for the treatment of PDAC and other cold tumors.",
        "stage": "Development",
        "readiness_level": "Experimental Proof",
        "expertise_required": "Immunology, Oncology",
        "resource_needs": {
            "Research and Development Support": [
                "Research Grants",
                "Translational Research Support",
                "Regulatory Support",
                "Patent and Market Research",
            ],
            "Mentorship and Support": [
                "Entrepreneurs in Residence",
                "Mentorship Programs",
            ],
            "Funding and Grants": [
                "Grants Programs",
                "Venture Funds",
            ],
        },
        "inventor": {
            "name": "Jenny Ting",
            "department": "Department of Microbiology and Immunology",
            "school": "School of Medicine",
            "role": "Faculty",
        },
    },
    {
        "id": "T4",
        "name": "Microfluidic Device for Human Vasculature Modeling",
        "techtype": "Biomedical Engineering",
        "short_description": "A microfluidic device developed to model human vasculature and hollow tissue structures, enabling precise control of the mechanical and chemical endothelial environments.",
        "long_description": "Researchers in the Department of Biomedical Engineering have developed a microfluidic device to model human vasculature and hollow tissue structures such as ducts and vessels. The device, made of polymer housing with alignment features, allows the generation of hollow tubes in hydrogels and biomaterials. It's designed for low cell numbers and reagent volumes, and is compatible with standard laboratory equipment. The device supports various assays under flow or static conditions, including permeability, solute transport, cell adhesion, angiogenesis, and hemostasis. It enables precise control over mechanical and chemical endothelial environments and is applicable to a range of research involving complex 3D flow. This technology is particularly relevant for studying various disease states and can be used in drug development and patient screening for clinical trials.",
        "stage": "Development",
        "readiness_level": "Prototype",
        "expertise_required": "Biomedical Engineering, Vascular Biology",
        "resource_needs": {
            "Research and Development Support": [
                "Fabrication Protocols",
                "Device Testing and Validation",
            ],
            "Technology and Infrastructure": [
                "Microfabrication Facilities",
                "Biomaterials Supply",
            ],
            "Market Research and Commercialization": [
                "Market Analysis for Biomedical Devices",
                "Commercialization Strategy Development",
            ],
        },
        "inventor": {
            "name": "Wubin Bai",
            "department": "Department of Applied Physical Sciences",
            "school": "College of Arts & Sciences",
            "role": "Facult",
        },
    },
    {
        "id": "T5",
        "name": "CVC Clave Management Tools",
        "techtype": "Medical Device",
        "short_description": "Innovative tools designed to mitigate the challenges associated with releasing a seized clave from central venous catheters (CVCs).",
        "long_description": "Researchers at UNC have developed two novel prototype devices to address the common issues in managing central venous catheters (CVCs), particularly in dealing with seized claves. These prototypes are tools that facilitate loosening attached claves and lumen hubs using a series of grips, allowing the user to easily apply torque to loosen the attachment joint. The need for such devices arises from the challenges faced by patients and caregivers, especially in home-care settings, where improper handling of claves can lead to overtightening, leading to difficulty in removal, or undertightening, which increases infection risks. The devices are slated for usability testing to optimize performance and address end-user needs.",
        "stage": "Prototype Development",
        "readiness_level": "Usability Testing",
        "expertise_required": "Medical Engineering, Patient Care",
        "resource_needs": {
            "Research and Development Support": [
                "Usability Testing",
                "Design Optimization",
            ],
            "Clinical Trials and Validation": [
                "Patient Safety Studies",
                "Efficacy Assessment",
            ],
            "Regulatory Compliance": [
                "FDA Approval Process",
                "Medical Device Certification",
            ],
        },
        "inventor": {
            "name": "Amy Cole",
            "department": "IT",
            "school": "School of Medicine",
            "role": "Staff",
        },
    },
]
