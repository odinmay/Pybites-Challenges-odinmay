import pytest

from workouts import print_workout_days


@pytest.mark.parametrize('workout, expected',
                         [('30', 'Wed'),
                          ('upper', 'Mon, Thu'),
                          ('lower', 'Tue, Fri'),
                          ('min', 'Wed'),
                          ('body', 'Mon, Tue, Thu, Fri'),
                          ('', 'Mon, Tue, Wed, Thu, Fri'),
                          ('test', 'No matching workout')])
def test_print_workout_days(capsys, workout, expected):
    print_workout_days(workout)
    # Capture output and strip whitespace
    # https://docs.pytest.org/en/latest/how-to/capture-stdout-stderr.html#
    out = capsys.readouterr().out.strip()
    assert out == expected

