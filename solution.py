import json

def calc_data(data):

    applicant = data['applicants']

    #print(applicant)

    score = 0 #random decimal
    scoredApplicants = []

    for person in applicant: #for all people in applicants
        score = get_score(applicant, person)
        scoredApplicants.append({'name': person['name'], 'score': round(score, 2)}) #add persons name + score

    #print(scoredApplicants)
    retFile = json.dumps({'scoredApplicants': scoredApplicants}, indent=4) #json.dumps returns json object, with the scoredApplicants, built in indent=4
    return retFile

def get_score(applicant, person):
    score = 0
    for attr in person['attributes']:
        if attr == 'spicyFoodTolerance':
            score += (person['attributes'][attr] / 100)
            #print(person['attributes'][attr] / 100)
        else:
            score += person['attributes'][attr] / 20
    return score




f = open('data.json')
jsonDict = json.load(f)
final = calc_data(jsonDict)
print(final)
