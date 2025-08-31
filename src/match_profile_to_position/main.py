#!/usr/bin/env python
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.match_profile_to_position.crew import MatchToProposalCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'path_to_jobs_csv': '/workspaces/crewai_projects/src/match_profile_to_position/data/jobs.csv',
        'path_to_cv': '/workspaces/crewai_projects/src/match_profile_to_position/data/cv.md'
    }
    MatchToProposalCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
