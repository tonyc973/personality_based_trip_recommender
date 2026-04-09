
def main(inputs: dict):
    from .crew import PersonalityBasedTripRecommenderCrew
    crew = PersonalityBasedTripRecommenderCrew()
    result = crew.kickoff(inputs=inputs)
    return result

if __name__ == "__main__":
    inputs = {
        "personality_traits": "adventurous, introvert"
    }
    output = main(inputs)
    print(output)