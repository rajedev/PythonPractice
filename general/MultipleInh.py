"""
Author: Rajendhiran Easu
Date: 25 Dec 2025
Description: Practice Multiple Inheritance on super keyword usage.
"""

class ResearchBase():
    def __init__(self, research_id: str, university: str):
        self.id = research_id
        self.university = university


class ResearchDomain():
    def __init__(self, domain_id: str, guide_name: str):
        self.domain_id = domain_id
        self.professor = guide_name


class TechResearch(ResearchBase, ResearchDomain):
    def __init__(self, r_id: str, d_id: str, guide, university: str, subject: str):
        self.subject = subject
        # super().__init__(research_id=f"{subject}-{r_id}", university=university)
        # super() is advisable in terms of single and multilevel, but best practice is to use ClassName.__init__(self,....)
        ResearchBase.__init__(self, research_id=f"{subject}-{r_id}", university=university)
        ResearchDomain.__init__(self, domain_id=d_id, guide_name=guide)


tech_research = TechResearch(r_id="RID1234", d_id="DID242", guide="Dr. Venkat Subramaniam", subject="Agentic AI",
                             university="Puducherry University")

print(tech_research.__dict__)
