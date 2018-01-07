 class BestCourse:
    website = "http://google.com"


    def __init__(self, name):
        self.name = name

course = BestCourse("Learn anything")
learn_command_line_course = BestCourse("Learn Command Line")

print(course.name)
print(BestCourse.website)

print(learn_command_line_course.name)
print(BestCourse.website)