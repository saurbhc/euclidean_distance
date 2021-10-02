import pandas as pd
import math


class EuclideanDistance:
    def __init__(self, _from_vector, _to_vector):
        self.from_vector = _from_vector
        self.to_vector = _to_vector
        self.from_vector_list = [int(_vector_coordinate_value) for _vector_coordinate_value in _from_vector.split(",")]
        self.to_vector_list = [int(_vector_coordinate_value) for _vector_coordinate_value in _to_vector.split(",")]

    def execute(self):
        data = [[self.from_vector, self.to_vector, self.compute_euclidean_distance()]]
        ed_df = pd.DataFrame(data, columns=['FromVector', 'ToVector', 'EuclideanDistance'])

        return ed_df

    def compute_euclidean_distance(self):
        return math.sqrt(
            sum(
                [(i - j) ** 2 for i, j in zip(self.from_vector_list, self.to_vector_list)]
            )
        )


if __name__ == "__main__":
    help_text = """Select an option (integer):

    1: Find Euclidean Distance between 2 n-dimension cartesian-coordinates.
    2: Find Euclidean Distance between multiple n-dimension cartesian-coordinate(s) with given same-dimension cartesian-coordinate

    (note) Send your suggestion on Saurabh.Chopra.2021@live.rhul.ac.uk for any suggestions.
    """

    print(help_text)
    choice = int(input(">"))
    if choice == 1:
        number_of_vectors = 2
        from_vector = None
        to_vector = None
        for vector_number in range(number_of_vectors):
            counter = vector_number + 1
            vector_or_cartesian_coordinate = input(
                f"!Enter comma-seperated-without-spaces values your `{counter}` vector/cartesian-coordinate (Example: 1,2,3): "
            )
            if not from_vector:
                from_vector = vector_or_cartesian_coordinate
            else:
                to_vector = vector_or_cartesian_coordinate
        ed = EuclideanDistance(_from_vector=from_vector, _to_vector=to_vector)
        euclidean_distance = ed.execute()
        print(f"""
>> Euclidean Distance is:
{euclidean_distance.to_string()}
""")
    elif choice == 2:
        from_vector = input(
            f"!Enter comma-seperated-without-spaces values your `test-coordinate` vector/cartesian-coordinate (Example: 1,2,3): "
        )
        number_of_vectors = int(input(f"How many coordinates would you like to compute the distance with your test-coordinate with? (Example: 3): "))
        euclidean_distance_df = pd.DataFrame()
        to_vector = None
        for vector_number in range(number_of_vectors):
            counter = vector_number + 1
            vector_or_cartesian_coordinate = input(
                f"!Enter comma-seperated-without-spaces values your `{counter}` vector/cartesian-coordinate (Example: 1,2,3): "
            )
            if not from_vector:
                from_vector = vector_or_cartesian_coordinate
            else:
                to_vector = vector_or_cartesian_coordinate
            ed = EuclideanDistance(_from_vector=from_vector, _to_vector=to_vector)
            ed_df = ed.execute()
            if euclidean_distance_df.empty:
                euclidean_distance_df = ed_df
            else:
                euclidean_distance_df = euclidean_distance_df.append(ed_df)

        print(f"""
>> Euclidean Distance Table:
{euclidean_distance_df.to_string()}
        """)
    else:
        print("Choose between below choices...", help_text)


