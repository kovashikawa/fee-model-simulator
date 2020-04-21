# The simulator tests are our integration tests

from click.testing import CliRunner
from fee_simulator.simulator import runAuctions


def test_different_simulation_numbers():
  runner = CliRunner()
  result = runner.invoke(runAuctions, ['5'])
  assert result.output == "Executing auction number 1\nExecuting auction number 2\nExecuting auction number 3\nExecuting auction number 4\nExecuting auction number 5\n"

  result = runner.invoke(runAuctions, ['1'])
  assert result.output == "Executing auction number 1\n"
