import re

def generate_cold_email(job_title, job_description, cv_text):

    job_description_processed = job_description.replace('About the job', 'The job is about ').replace('Job overview', 'This position entails ').replace('Role overview', 'The role primarily focuses on ').replace('Position summary', 'This position summary highlights ').replace('About the role', 'The role involves ').replace('Job details', 'The details of the job are ').replace('Responsibilities', 'The responsibilities include ').replace('Key responsibilities', 'Some key responsibilities are ').replace('Primary responsibilities', 'The primary tasks and responsibilities are ').replace('Main responsibilities', 'Main tasks and duties include ').replace('Duties', 'The duties include ').replace('What you will do', 'In this role, you will ').replace('Job requirements', 'The requirements for this role include ').replace('Requirements', 'The required qualifications are ').replace('Required qualifications', 'Mandatory qualifications for the role are ').replace('Minimum qualifications', 'The minimum qualifications required are ').replace('Preferred qualifications', 'Preferred qualifications include ').replace('Qualifications', 'Essential qualifications for the role are ').replace('Experience required', 'Experience needed for this job is ').replace('Skills required', 'The skills required are ').replace('Desired skills', 'The desired skill set includes ').replace('Required skills', 'Mandatory skills for the role are ').replace('Key qualifications', 'The qualifications for this position are ').replace('Who you are', 'Ideal candidates are ').replace('Who we are looking for', 'We are seeking ').replace('What we are looking for', 'The ideal candidate should have ').replace('Your profile', 'Candidate profile should include ').replace('Role summary', 'Role summary describes ').replace('Candidate profile', 'The profile for the ideal candidate includes ').replace('What you will bring', 'You will bring to the team ').replace('What you need', 'You will need ').replace('About us', 'Information about the company: ').replace('Who we are', 'We are a company focused on ').replace('Our mission', 'Our mission is ').replace('Company overview', 'Here is an overview of our company: ').replace('Additional requirements', 'The additional requirements are ').replace('Additional qualifications', 'Other qualifications include ').replace('Nice-to-have skills', 'Preferred skills are ').replace('Perks and benefits', 'The perks and benefits include ').replace('Benefits', 'Advantages of working in this role include ').replace('Work environment', 'The work environment involves ').replace('Why join us', 'Reasons to join us include ').replace('What we offer', 'We offer ').replace('Job location', 'The location for this job is ').replace('Compensation', 'Compensation for this role is ').replace('Pay scale', 'The pay scale is ').replace('Salary', 'Salary offered is ').replace('Job title', 'The title of the job is ')
    job_description_processed = job_description_processed.lower().replace('.', ',')
    job_description_paragraph = " ".join(job_description_processed.splitlines()).strip()

    relevant_sections = {}
    for section in ["Education", "Certifications", "Projects", "Skills"]:
        pattern = rf"{section}[:\s]*([\s\S]*?)(?=\n[A-Z]|\n\n|$)"
        match = re.search(pattern, cv_text, re.DOTALL | re.IGNORECASE)
        if match:
            relevant_sections[section] = match.group(1).strip().replace("\n", " ")

    education = relevant_sections.get("Education", "a strong educational background relevant to the position")
    certifications = relevant_sections.get("Certifications", "relevant certifications in the industry")
    projects = relevant_sections.get("Projects", "significant hands-on experience in relevant domains")
    skills = relevant_sections.get("Skills", "key skills aligning with the job requirements")

    cold_email = f"""
    Subject: Application for {job_title} Position

    Dear Hiring Manager,

    I hope you're doing well. I recently came across the {job_title} opening at your company and was thrilled by the opportunity to apply.
    The role resonates with me due to its focus on {job_description_paragraph}, which perfectly aligns with my skills and experience.

    With my educational background in {education}, I have developed expertise in {skills}, which align closely with the requirements mentioned in the job description. My certifications include {certifications}, and my projects include {projects}. These experiences have sharpened my technical abilities and problem-solving skills, making me a strong candidate for this role.

    I am confident that my qualifications and enthusiasm for this position would allow me to contribute meaningfully to your team. I would welcome the chance to discuss my application and how I can support your company’s objectives.

    Thank you for considering my application. I look forward to the opportunity to connect with you.
    
    Best regards,  
    [Your Name]
    """

    return cold_email
