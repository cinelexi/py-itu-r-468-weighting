from collections import namedtuple
from math import inf

# GLOBAL_DB_TOLERANCE was determined by taking the maximum value of the
# difference between computed ("1khz" and "2khz" option) and expected ITU-R 468
# values. If the r468 function improves over time, this constant should
# converge to 0.
GLOBAL_DB_TOLERANCE = 0.07184434988229427

TestDatum = namedtuple(
    "TestDatum",
    ["frequency", "expected_db", "lower_tolerance", "upper_tolerance", "khz_option"],
)

ITU_R_468__FREQS_AND_EXP_VALS = [
    TestDatum(
        frequency=31.5,
        expected_db=-29.9,
        lower_tolerance=-2.0,
        upper_tolerance=2.0,
        khz_option="1khz",
    ),
    TestDatum(
        frequency=63,
        expected_db=-23.9,
        lower_tolerance=-1.4,
        upper_tolerance=1.4,
        khz_option="1khz",
    ),
    TestDatum(
        frequency=100,
        expected_db=-19.8,
        lower_tolerance=-1.0,
        upper_tolerance=1.0,
        khz_option="1khz",
    ),
    TestDatum(
        frequency=200,
        expected_db=-13.8,
        lower_tolerance=-0.85,
        upper_tolerance=0.85,
        khz_option="1khz",
    ),
    TestDatum(
        frequency=400,
        expected_db=-7.8,
        lower_tolerance=-0.7,
        upper_tolerance=0.7,
        khz_option="1khz",
    ),
    TestDatum(
        frequency=800,
        expected_db=-1.9,
        lower_tolerance=-0.55,
        upper_tolerance=0.55,
        khz_option="1khz",
    ),
    TestDatum(
        frequency=1000,
        expected_db=0.0,
        lower_tolerance=-0.5,
        upper_tolerance=0.5,
        khz_option="1khz",
    ),
    TestDatum(
        frequency=2000,
        expected_db=5.6,
        lower_tolerance=-0.5,
        upper_tolerance=0.5,
        khz_option="1khz",
    ),
    TestDatum(
        frequency=3150,
        expected_db=9.0,
        lower_tolerance=-0.5,
        upper_tolerance=0.5,
        khz_option="1khz",
    ),
    TestDatum(
        frequency=4000,
        expected_db=10.5,
        lower_tolerance=-0.5,
        upper_tolerance=0.5,
        khz_option="1khz",
    ),
    TestDatum(
        frequency=5000,
        expected_db=11.7,
        lower_tolerance=-0.5,
        upper_tolerance=0.5,
        khz_option="1khz",
    ),
    TestDatum(
        frequency=6300,
        expected_db=12.2,
        lower_tolerance=0.0,
        upper_tolerance=0.0,
        khz_option="1khz",
    ),
    TestDatum(
        frequency=7100,
        expected_db=12.0,
        lower_tolerance=-0.2,
        upper_tolerance=0.2,
        khz_option="1khz",
    ),
    TestDatum(
        frequency=8000,
        expected_db=11.4,
        lower_tolerance=-0.4,
        upper_tolerance=0.4,
        khz_option="1khz",
    ),
    TestDatum(
        frequency=9000,
        expected_db=10.1,
        lower_tolerance=-0.6,
        upper_tolerance=0.6,
        khz_option="1khz",
    ),
    TestDatum(
        frequency=10000,
        expected_db=8.1,
        lower_tolerance=-0.8,
        upper_tolerance=0.8,
        khz_option="1khz",
    ),
    TestDatum(
        frequency=12500,
        expected_db=0.0,
        lower_tolerance=-1.2,
        upper_tolerance=1.2,
        khz_option="1khz",
    ),
    TestDatum(
        frequency=14000,
        expected_db=-5.3,
        lower_tolerance=-1.4,
        upper_tolerance=1.4,
        khz_option="1khz",
    ),
    TestDatum(
        frequency=16000,
        expected_db=-11.7,
        lower_tolerance=-1.6,
        upper_tolerance=1.6,
        khz_option="1khz",
    ),
    TestDatum(
        frequency=20000,
        expected_db=-22.2,
        lower_tolerance=-2.0,
        upper_tolerance=2.0,
        khz_option="1khz",
    ),
    TestDatum(
        frequency=31500,
        expected_db=-42.7,
        lower_tolerance=-inf,
        upper_tolerance=2.8,
        khz_option="1khz",
    ),
    TestDatum(
        frequency=31.5,
        expected_db=-35.5,
        lower_tolerance=-2.0,
        upper_tolerance=2.0,
        khz_option="2khz",
    ),  # Revert 31 to 31.5 Hz, assume mistake in SMPTE RP
    TestDatum(
        frequency=63,
        expected_db=-29.5,
        lower_tolerance=-1.4,
        upper_tolerance=1.4,
        khz_option="2khz",
    ),
    TestDatum(
        frequency=100,
        expected_db=-25.4,
        lower_tolerance=-1.0,
        upper_tolerance=1.0,
        khz_option="2khz",
    ),
    TestDatum(
        frequency=200,
        expected_db=-19.4,
        lower_tolerance=-0.85,
        upper_tolerance=0.85,
        khz_option="2khz",
    ),
    TestDatum(
        frequency=400,
        expected_db=-13.4,
        lower_tolerance=-0.7,
        upper_tolerance=0.7,
        khz_option="2khz",
    ),
    TestDatum(
        frequency=800,
        expected_db=-7.5,
        lower_tolerance=-0.55,
        upper_tolerance=0.55,
        khz_option="2khz",
    ),
    TestDatum(
        frequency=1000,
        expected_db=-5.6,
        lower_tolerance=-0.5,
        upper_tolerance=0.5,
        khz_option="2khz",
    ),
    TestDatum(
        frequency=2000,
        expected_db=0.0,
        lower_tolerance=-0.5,
        upper_tolerance=0.5,
        khz_option="2khz",
    ),
    TestDatum(
        frequency=3150,
        expected_db=3.4,
        lower_tolerance=-0.5,
        upper_tolerance=0.5,
        khz_option="2khz",
    ),
    TestDatum(
        frequency=4000,
        expected_db=4.9,
        lower_tolerance=-0.5,
        upper_tolerance=0.5,
        khz_option="2khz",
    ),
    TestDatum(
        frequency=5000,
        expected_db=6.1,
        lower_tolerance=-0.5,
        upper_tolerance=0.5,
        khz_option="2khz",
    ),
    TestDatum(
        frequency=6300,
        expected_db=6.6,
        lower_tolerance=0.0,
        upper_tolerance=0.0,
        khz_option="2khz",
    ),
    TestDatum(
        frequency=7100,
        expected_db=6.4,
        lower_tolerance=-0.2,
        upper_tolerance=0.2,
        khz_option="2khz",
    ),
    TestDatum(
        frequency=8000,
        expected_db=5.8,
        lower_tolerance=-0.4,
        upper_tolerance=0.4,
        khz_option="2khz",
    ),
    TestDatum(
        frequency=9000,
        expected_db=4.5,
        lower_tolerance=-0.6,
        upper_tolerance=0.6,
        khz_option="2khz",
    ),
    TestDatum(
        frequency=10000,
        expected_db=2.5,
        lower_tolerance=-0.8,
        upper_tolerance=0.8,
        khz_option="2khz",
    ),
    TestDatum(
        frequency=12500,
        expected_db=-5.6,
        lower_tolerance=-1.2,
        upper_tolerance=1.2,
        khz_option="2khz",
    ),
    TestDatum(
        frequency=14000,
        expected_db=-10.9,
        lower_tolerance=-1.4,
        upper_tolerance=1.4,
        khz_option="2khz",
    ),
    TestDatum(
        frequency=16000,
        expected_db=-17.3,
        lower_tolerance=-1.65,
        upper_tolerance=1.65,
        khz_option="2khz",
    ),
    TestDatum(
        frequency=20000,
        expected_db=-27.8,
        lower_tolerance=-2.0,
        upper_tolerance=2.0,
        khz_option="2khz",
    ),
    TestDatum(
        frequency=31500,
        expected_db=-48.3,
        lower_tolerance=-inf,
        upper_tolerance=2.8,
        khz_option="2khz",
    ),
]
