class GradeTracker:
    def __init__(self):
        self.tests = []

    def add_assingment(self, test):
        self.tests.append(test)

    def list_assingments(self, tests=None):
        items = tests if tests is not None else self.tests
        if not items:
            print("\nNo assignments to display.\n")
            return
        print("\n" + "-" * 90)
        for test in items:
            print(test)
        print("-" * 90 + f"\nTotal: {len(items)} assignment(s)\n")

    def filter_by_subject(self, subject):
        subject = subject.strip().lower()
        return [test for test in self.tests if test.subject == subject]

    def filter_by_type(self, atype):
        atype = atype.lower()
        return [test for test in self.tests if test.atype == atype]

    def filter_by_month(self, month):
        return [test for test in self.tests if test.due_date.startswith(month)]

    def show_grade_summary(self):
        if not self.tests:
            print("\n[!] No tests found. Add entry first")
            return

        def get_percentage(e):
            return (e.score / e.max_score) * 100

        total_percentage = sum(get_percentage(e) for e in self.tests)
        average = total_percentage / len(self.tests)

        high = max(self.tests, key=get_percentage)
        low = min(self.tests, key=get_percentage)

        print("\n" + "=" * 40)
        print("   GRADE SUMMARY")
        print("=" * 40)

        print(f"Overall average grade: {average:.1f}%")

        print("\nPer-subject averages:")
        subjects = sorted(set(test.subject for test in self.tests))

        for subject in subjects:
            filtered = [test for test in self.tests if test.subject == subject]
            subject_score = sum(test.score for test in filtered)
            subject_max_score = sum(test.max_score for test in filtered)
            subject_average = (subject_score / subject_max_score) * 100
            print(f"- {subject.title()}: {subject_average:.1f}%")

        print(f"Highest grade: {high.subject.title()} ({get_percentage(high):.1f}%)")
        print(f"Lowest grade: {low.subject.title()} ({get_percentage(low):.1f}%)")