# The simulator tests are our integration tests

from click.testing import CliRunner
from fee_simulator.simulator import run_auctions


def test_different_simulation_numbers():
  runner = CliRunner()
  result = runner.invoke(run_auctions, ['5'])
  assert result.output == "Executing auction number 1\nExecuting auction number 2\nExecuting auction number 3\nExecuting auction number 4\nExecuting auction number 5\n"

  result = runner.invoke(run_auctions, ['1'])
  assert result.output == "Executing auction number 1\n"

def test_csv_output():
  runner = CliRunner()
  result = runner.invoke(run_auctions, ['1', '--outputfile', 'resultsTest.csv'])
  assert result.output == "Executing auction number 1\n"

  file = open("resultsTest.csv", 'r', newline='')
  assert "Timestep,BidValue,BidWeight,CreationTimestep" in file.read()

