import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.job_posting.crew import JobPostingCrew


def run():
    inputs = {
        'company_domain': 'careers.wbd.com',
        'company_description': "Warner Bros. Discovery is a premier global media and entertainment company, offering audiences the world’s most differentiated and complete portfolio of content, brands and franchises across television, film, sports, news, streaming and gaming. We're home to the world’s best storytellers, creating world-class products for consumers",
        "hiring_needs": "We are looking for a talented Software Engineer to join our dynamic team. The ideal candidate will have experience in developing scalable web applications, a strong understanding of cloud technologies, and a passion for innovation. Responsibilities include designing, coding, and testing software solutions, collaborating with cross-functional teams, and staying updated with the latest industry trends.",
        "specific_requirements": "Bachelor's degree in Computer Science or related field, 3+ years of experience in software development, proficiency in Python and JavaScript, experience with AWS or Azure, strong problem-solving skills, excellent communication and teamwork abilities.",
        "job_title": "Software Engineer",
        'specific_benefits':'Weekly Pay, Employee Meals, healthcare',
        "location": "New York, NY",
        "job_type": "Full-time",
        "salary_range": "$80,000 - $120,000",
        "application_deadline": "2024-12-31",
        "additional_info": "We offer a competitive salary, comprehensive benefits, and opportunities for professional growth. Join us in shaping the future of media and entertainment!"
    }
    JobPostingCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'company_domain':'careers.wbd.com',
        'company_description': "Warner Bros. Discovery is a premier global media and entertainment company, offering audiences the world’s most differentiated and complete portfolio of content, brands and franchises across television, film, sports, news, streaming and gaming. We're home to the world’s best storytellers, creating world-class products for consumers",
        'hiring_needs': 'Production Assistant, for a TV production set in Los Angeles in June 2025',
        'specific_benefits':'Weekly Pay, Employee Meals, healthcare',
    }
    try:
        JobPostingCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


if __name__ == "__main__":
    run()
