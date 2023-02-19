#!/bin/bash

num1=1
num2=10

case $op in
    1)
        result=$((num1 + num2))
        echo "Result: $result"
        ;;
    2)
        result=$((num1 - num2))
        echo "Result: $result"
        ;;
    3)
        result=$((num1 * num2))
        echo "Result: $result"
        ;;
    4)
        result=$((num1 / num2))
        echo "Result: $result"
        ;;
    *)
        echo "Invalid option selected"
        ;;
esac
