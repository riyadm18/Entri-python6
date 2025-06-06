{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4a52102f-af43-4641-adc6-63108dbb25e2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Core Course Details:\n",
      "Course Code: CS101\n",
      "Course Name: Introduction to Computer Science\n",
      "Credit Hours: 3\n",
      "Required for Major: Yes\n",
      "\n",
      "Elective Course Details:\n",
      "Course Code: HIST201\n",
      "Course Name: World History\n",
      "Credit Hours: 2\n",
      "Elective Type: liberal arts\n"
     ]
    }
   ],
   "source": [
    "# Base class\n",
    "class Course:\n",
    "    def __init__(self, course_code, course_name, credit_hours):\n",
    "        self.course_code = course_code\n",
    "        self.course_name = course_name\n",
    "        self.credit_hours = credit_hours\n",
    "\n",
    "    def display_info(self):\n",
    "        print(f\"Course Code: {self.course_code}\")\n",
    "        print(f\"Course Name: {self.course_name}\")\n",
    "        print(f\"Credit Hours: {self.credit_hours}\")\n",
    "\n",
    "# Subclass for Core Course\n",
    "class CoreCourse(Course):\n",
    "    def __init__(self, course_code, course_name, credit_hours, required_for_major):\n",
    "        super().__init__(course_code, course_name, credit_hours)\n",
    "        self.required_for_major = required_for_major\n",
    "\n",
    "    def display_info(self):\n",
    "        super().display_info()\n",
    "        print(f\"Required for Major: {'Yes' if self.required_for_major else 'No'}\")\n",
    "\n",
    "# Subclass for Elective Course\n",
    "class ElectiveCourse(Course):\n",
    "    def __init__(self, course_code, course_name, credit_hours, elective_type):\n",
    "        super().__init__(course_code, course_name, credit_hours)\n",
    "        self.elective_type = elective_type\n",
    "\n",
    "    def display_info(self):\n",
    "        super().display_info()\n",
    "        print(f\"Elective Type: {self.elective_type}\")\n",
    "\n",
    "# Sample usage\n",
    "if __name__ == \"__main__\":\n",
    "    core = CoreCourse(\"CS101\", \"Introduction to Computer Science\", 3, True)\n",
    "    elective = ElectiveCourse(\"HIST201\", \"World History\", 2, \"liberal arts\")\n",
    "\n",
    "    print(\"\\nCore Course Details:\")\n",
    "    core.display_info()\n",
    "\n",
    "    print(\"\\nElective Course Details:\")\n",
    "    elective.display_info()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5e52dfe0-c2c6-4954-b501-3745728810e8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
