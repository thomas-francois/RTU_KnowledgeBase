from logic import *
from pprint import pprint

# Define symbols:
Rain = Symbol("Rain")
Traffic = Symbol("Traffic")
Meeting = Symbol("Meeting")
Strike = Symbol("Strike")

WFH = Symbol("WFH")
Drive = Symbol("Drive")
PublicTransport = Symbol("PublicTransport")


# Define the (rules):
rule_wfh = Or(Rain, Meeting)
rule_drive = And(Not(Rain), Not(Traffic))
rule_public_transport = And(Not(Strike), Not(Rain))

# Define knowledge base
knowledge_base = And(
    Implication(rule_wfh, WFH),
    Implication(rule_drive, Drive),
    Implication(rule_public_transport, PublicTransport)
)


scenario1 = And(Not(Rain), Traffic, Not(Meeting), Not(Strike))
scenario2 = And(Not(Rain), Not(Traffic), Not(Meeting), Not(Strike))
scenario3 = And(Rain, Not(Traffic), Meeting, Strike)

# Define the queries
query_WFH = WFH
query_Drive = Drive
query_PublicTransport = PublicTransport


def check_all_scenarios(knowledge_base):
    return {
        "Scenario 1": {
            "Formula": scenario1.formula(),
            "workFromHome": model_check(And(knowledge_base, scenario1), query_WFH),
            "drive": model_check(And(knowledge_base, scenario1), query_Drive),
            "publicTransport": model_check(And(knowledge_base, scenario1), query_PublicTransport),
        },
        "Scenario 2": {
            "Formula": scenario2.formula(),
            "workFromHome": model_check(And(knowledge_base, scenario2), query_WFH),
            "drive": model_check(And(knowledge_base, scenario2), query_Drive),
            "publicTransport": model_check(And(knowledge_base, scenario2), query_PublicTransport),
        },
        "Scenario 3": {
            "Formula": scenario3.formula(),
            "workFromHome": model_check(And(knowledge_base, scenario3), query_WFH),
            "drive": model_check(And(knowledge_base, scenario3), query_Drive),
            "publicTransport": model_check(And(knowledge_base, scenario3), query_PublicTransport),
        },
}

print("First set of conditions :")
pprint(check_all_scenarios(knowledge_base))



# Add symbols for second part:
Appointment = Symbol("Appointment")
RoadConstruction = Symbol("RoadConstruction")


# Update knowledge base:
new_knowledge_base = And(
    knowledge_base,
    Implication(Appointment, Drive),
    Implication(RoadConstruction, Or(PublicTransport, WFH))
)

# Update scenarios:
scenario1 = And(scenario1, Appointment, Not(RoadConstruction))
scenario2 = And(scenario2, Not(Appointment), Not(RoadConstruction))
scenario3 = And(scenario3, Appointment, RoadConstruction)

print("\n\n\nSecond set of conditions with added rules:")
pprint(check_all_scenarios(new_knowledge_base))
