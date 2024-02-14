# to run these, run 
# pytest test/test-validator.py

from guardrails import Guard
from validator import WebSanitization
guard = Guard.from_string(validators=[WebSanitization(on_fail='refrain')])


# def test_pass():
#   test_output = "a test value"
#   raw_output, guarded_output, *rest = guard.parse(test_output)
#   assert(guarded_output is test_output)

# def test_fail():
#   test_output = "b test value"
#   raw_output, guarded_output, *rest = guard.parse(test_output)
#   assert(guarded_output is None)
# import esprima

# Example usage
mixed_string_without_code = "This is just a regular string with no injected code."
mixed_string_with_code = """
    This is some text.
    <script>evil()</script>
"""

mixed_string_with_code_2 = """
    This is some text.
    <script>
    function hax() {
        console.log('hax')
    } hax(); And some more text here
"""


def test_pass():
  res = guard.parse(mixed_string_without_code)
  assert(res.validated_output == mixed_string_without_code)

def test_fail():
  res = guard.parse(mixed_string_with_code)
  assert(res.validated_output is None) 

  res = guard.parse(mixed_string_with_code_2)
  assert(res.validated_output is None) 

