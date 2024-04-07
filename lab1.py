#Lab 1; Juliette P
x = 0
while x < 10:
    x = x + 2
    print(x)

#Q2
print("There is a rectangle, of which one side is 3 and the other side is 4.")
side_1 = 3
side_2 = 4
print(f"I think the area of the rectangle is:{(side_1) + (side_2)}")

#Q3
prof_name = 'Alice'
me = "Juliette"
my_github_acnt = "https://github.com/hiimjuliettep"
my_hobby = "learning about coding :)" 
hours_practiced_per_week = '4 hours'

coding_exp = ["newbie", "beginner", "intermediate", "advanced"]
my_coding_exp = coding_exp[0]

project_types = ['game developement', 'website_applications', 'data_analysis', 'machine_learning']
project_interest = project_types[1]
project_interest_2 = project_types[2]

print(f"""

Hi {prof_name}

My name is {me}. I love {my_hobby}!

My experience in coding I think is {my_coding_exp}.
I've really enjoyed learning coding {hours_practiced_per_week} per week.
Projects I'd like to continue learning {project_interest} and {project_interest_2}.
My Github account is {my_github_acnt}.

I'm very grateful for all the work you've done to help me learn 
computer science!!

Cheers,
{me}
""")