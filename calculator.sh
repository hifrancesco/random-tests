#!/bin/bash

echo "Welcome to the calculator!"

while true; do
  # Prompt the user for the operation to perform
  echo "Please enter the operation to perform: +, -, *, / (or q to quit)"
  read operation

  # Quit the script if the user enters 'q'
  if [[ "$operation" == "q" ]]; then
    echo "Exiting the calculator."
    exit 0
  fi

  # Prompt the user for the operands
  echo "Please enter the first operand:"
  read operand1
  echo "Please enter the second operand:"
  read operand2

  # Perform the calculation based on the selected operation
  case "$operation" in
    "+")
      result=$(echo "$operand1 + $operand2" | bc)
      ;;
    "-")
      result=$(echo "$operand1 - $operand2" | bc)
      ;;
    "*")
      result=$(echo "$operand1 * $operand2" | bc)
      ;;
    "/")
      result=$(echo "scale=2; $operand1 / $operand2" | bc)
      ;;
    *)
      echo "Invalid operation. Please try again."
      continue
      ;;
  esac

  # Display the result to the user
  echo "The result of $operand1 $operation $operand2 is $result."
done
