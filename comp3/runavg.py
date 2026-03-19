# just to quickly check the evaluate score
import sys
import subprocess
import os
import pandas as pd

# env LD_LIBRARY_PATH="" python ./testing/inception_score.py ./inference/epoch_010_new ./output/score.csv 39
def average_score(csv_path):
    df = pd.read_csv(csv_path)
    return df['score'].mean()


def run_evaluation(inference_path):
    env = os.environ.copy()
    env["LD_LIBRARY_PATH"] = ""

    subprocess.run(
        [
            "python",
            "./testing/inception_score.py",
            inference_path,
            "./output/score.csv",
            "39"
        ],
        env=env,
        check=True
    )


def main():
    # Need at least 1 argument
    if len(sys.argv) < 2:
        print("Usage: python runavg.py <0|1> [inference_path]")
        sys.exit(1)

    evaluate = sys.argv[1]  # "0" or "1"

    if evaluate == "1":
        # Check for inference path
        if len(sys.argv) < 3:
            print("Error: Must provide inference path when evaluate = 1")
            sys.exit(1)

        inference_path = sys.argv[2]
        print(f"Running evaluation on: {inference_path}")
        run_evaluation(inference_path)

    elif evaluate == "0":
        print("Skipping evaluation (as requested).")

    else:
        print("Error: First argument must be 0 or 1")
        sys.exit(1)

    # Always compute the average after evaluation or skipping
    csv_file = "output/score.csv"
    print("Average score:", average_score(csv_file))


if __name__ == "__main__":
    main()
