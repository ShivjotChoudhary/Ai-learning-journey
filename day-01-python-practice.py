{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ShivjotChoudhary/ai-learning-journey/blob/main/day-01-python-practice.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PsQ9w-OQmTNQ",
        "outputId": "01bdb2f8-8c66-4367-977e-9b0280fb961f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "hello  my name is shivjot choudhary\n"
          ]
        }
      ],
      "source": [
        "print(\"hello  my name is shivjot choudhary\")"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Date = 14/1/2026 Questions:-"
      ],
      "metadata": {
        "id": "vx6DanNzxCCr"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Q1 SimpleInterest\n",
        "p= float(input(\"Enter. principal amount:\"))\n",
        "r =float(input(\"Enter rate:\"))\n",
        "t=float(input(\"Enter time: \"))\n",
        "\n",
        "si = (p*r*t)/100\n",
        "print(\"Simple Interest is:\",si)"
      ],
      "metadata": {
        "id": "pdeynL0nnjqm",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "99e53876-81d3-46be-9698-bc179b278ea9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter. principal amount:10000\n",
            "Enter rate:10\n",
            "Enter time: 2\n",
            "Simple Interest is: 2000.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Q2 CompoundInterest\n",
        "p = float(input(\"Enter principal amount:\"))\n",
        "r=float(input(\"Enter rate:\"))\n",
        "t= float(input(\"Enter time: \"))\n",
        "\n",
        "ci = p*(1+r/100)**t\n",
        "print(\"Compound Interest:\", ci)\n",
        "\n"
      ],
      "metadata": {
        "id": "3Vcrjrb7rIyJ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0c96afec-5a34-47b5-acfd-b79d110a9335"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter principal amount:100000\n",
            "Enter rate:10\n",
            "Enter time: 2\n",
            "Compound Interest: 121000.00000000001\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Q 3) Area of Circle\n",
        "r=float(input(\"Enter  radius: \"))\n",
        "\n",
        "area = 3.14*r*r\n",
        "print(\"Area of circle:\", area)\n",
        "\n"
      ],
      "metadata": {
        "id": "HuvbyP3ArIvB",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b9ed69c9-5159-4ec3-e8aa-50346e7fd201"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter  radius: 2\n",
            "Area of circleis: 12.56\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Q4 Area ofTriangle\n",
        "b=float(input(\"Enter base: \"))\n",
        "h=float(input(\"Enter height: \"))\n",
        "\n",
        "area = 0.5*b*h\n",
        "print(\"Area :\", area)\n",
        "\n"
      ],
      "metadata": {
        "id": "5ZLryWoKrIsJ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "97e923b6-0929-44f2-a694-a09bd4169327"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enterbase: 20\n",
            "Enter height: 1\n",
            "Area : 10.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Q5 Area of Rectangle\n",
        "l=float(input(\"length:\"))\n",
        "w=float(input(\"width\"))\n",
        "\n",
        "area = l*w\n",
        "print(\"Area:\", area)\n"
      ],
      "metadata": {
        "id": "MDxVfAAcrIpk",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "681f56a5-b692-40d5-bbfe-7141f76061e6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "length:2\n",
            "width2\n",
            "Area: 4.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Q6 Distance calculation\n",
        "speed =float(input(\"speed: \"))\n",
        "time=float(input(\"Enter time: \"))\n",
        "\n",
        "distance=speed * time\n",
        "print(\"Distance:\", distance)\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "rVJTUQ-rrIm8",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "9c98128a-26a8-4050-a5e0-8c7de840c77a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "speed: 2\n",
            "Enter time: 2\n",
            "Distance: 4.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "#Q7 Speedcalculation\n",
        "d=float(input(\"distance: \"))\n",
        "t=float(input(\"Enter time: \"))\n",
        "\n",
        "speed = d/t\n",
        "print(\"Speed:\", speed)\n"
      ],
      "metadata": {
        "id": "FaE2bV1irIkE",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "9112cd91-0faa-42b6-d1c6-28d2adc43d8d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "distance: 2\n",
            "Enter time: 3\n",
            "Speed: 0.6666666666666666\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "# Q8--BMI calculation\n",
        "weight=float(input(\"weight in kg:\"))\n",
        "height=float(input(\"height in meters:\"))\n",
        "\n",
        "bmi=weight/(height * height)\n",
        "print(\"BMI:\", bmi)\n"
      ],
      "metadata": {
        "id": "NBfiDMhUrIhd",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6086ada4-b24d-442d-ce6f-f3aea7c9304b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "weight in kg:3\n",
            "height in meters:4\n",
            "BMI: 0.1875\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "# Q9-Celsius to  Fahrenheit))\n",
        "c=float(input(\"Enter temperature in celsius:\"))\n",
        "f=(c * 9/5) +32\n",
        "print(\"Temperature:\", f)\n",
        "\n"
      ],
      "metadata": {
        "id": "XC6a9qYtrIe3",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5df8bec0-9347-4d89-c851-e1a69ccd973b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter temperature in celsius:33\n",
            "Temperature: 91.4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Q10 Perimeter of Rectangle:----\n",
        "l=float(input(\"Enterlength:\"))\n",
        "w=float(input(\"Enter width:\"))\n",
        "\n",
        "perimeter = 2 * (l + w)\n",
        "print(\"Perimeter:\", perimeter)"
      ],
      "metadata": {
        "id": "MEzu2q_orIb_",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e5ce1c7b-6a06-4431-bbf3-4d2e21832f19"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enterlength:22\n",
            "Enter width:22\n",
            "Perimeter: 88.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Q11)write a program to input two int number a and b , print true if a is greater than or eqaul to b . if not print false.\n",
        "a=int(input(\"1st number:\"))\n",
        "b=int(input(\" 2nd number:\"))\n",
        "print(a>b)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rYAXnsqVn-9c",
        "outputId": "eb14535d-3efb-432f-9b2d-482e4ff3cbd9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1st number:22\n",
            " 2nd number:33\n",
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\"\"\"q11 ) checking the modulo / remainder\n",
        "operator \"\"\"\n",
        "#it gives the value -ve when  -ve/-ve and +ve/-ve :)\n",
        "a,b=-9,-6\n",
        "print(a%b)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IGvDVbi_qtvR",
        "outputId": "5992c22a-de6a-4448-d8db-f11786615016"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "-3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Function practice :-**"
      ],
      "metadata": {
        "id": "RlIBlUA0wpPD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Q12)--concatenation of  two strings :-\n",
        "str1 = \"shivjot \"\n",
        "str2 = \"Choudhary\"\n",
        "final=str1+str2\n",
        "print(\"result:\",final)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2Q7FpZj_tZhx",
        "outputId": "56131708-70e8-490b-d140-3944b3d1dce7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "result: shivjot Choudhary\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Q13 basic functions :(len())\n",
        "\n",
        "a = \"shivjot\"\n",
        "print(len(a))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YXM7D6HnwQ6l",
        "outputId": "82a28544-d156-4305-eb8e-a15d1b6ec10f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "7\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Q14 indexing\n",
        "a = \"shivjot\"\n",
        "print(\"->\",a[4],\"\\n\",a[0:4])"
      ],
      "metadata": {
        "id": "jxxHD31CTmLE",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a07ea87e-c0dc-4799-bed9-f7c6ae718a83"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "-> j \n",
            " shiv\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#15 checking the first letter of the sentence is vowel or consonant\n",
        "a = str(input(\"Enter the sentence : \"))\n",
        "b = \"aeiou\"\n",
        "if a[0]== b[0] or  a[0]== b[1] or a[0]==b[2] or a[0]==b[3] or a[0]== b[4]: #Also we can simply use (a[0] in b)<----\n",
        "  print(\"First letter is : Vowel\")\n",
        "else :\n",
        "  print(\"First letter is : Consonant\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "k--XJEtJTnZe",
        "outputId": "e2ac5a5f-a014-4681-8daa-2277dc15e138"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the sentence : adi\n",
            "First letter is : Vowel\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# q16 minus indexing :-\n",
        "a= \"apple\"\n",
        "print(a[-2:])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QxTAYQ_ErceY",
        "outputId": "67fe2257-4388-4ff4-fb3c-904e392d1d6e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "le\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Q17 using .endswith(\"\")#returns boolean value\n",
        "str=\"shivjot\"\n",
        "print(str.endswith(\"ot\"))  #str.endswith(\"\") returns true if string ends with substr"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aJrm-dOYu-ig",
        "outputId": "c58fce5d-ef62-4902-b772-5fc642db35f5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#q18 using capitalize () function #it capitalizes the first  index.\n",
        "a=\"shivjot\"\n",
        "print(a.capitalize())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "R_Gh_wxdwyJJ",
        "outputId": "1d9f5575-69df-43a1-8ca1-7fb88c364b05"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Shivjot\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#q19 using replace(\"\")\n",
        "a=\"clock\"\n",
        "print(a.replace(\"loc\",\"oo\"))"
      ],
      "metadata": {
        "id": "34yXW6bcyBeH",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1cd53e1e-be7b-468d-f66e-0f312794b024"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "cook\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Q20 wap to input user's first name and print its length. #length() function\n",
        "a = input(\"enter your first Name: \")\n",
        "print(len(a))\n",
        "a.count(\"i\")"
      ],
      "metadata": {
        "id": "RBXZ7CM76S0A",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "69772f41-00f9-4b8a-ec47-da21d1b2bf63"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter your first Name: shivjot\n",
            "shivjot\n",
            "7\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Q21) list exp :-\n",
        "a = [\"shivjot\",99,98.7,\"python\"]\n",
        "a[3]=\"java\"\n",
        "print(a[-3:-1])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dNZU6t-cOzim",
        "outputId": "56b3a0f9-8f76-4c76-ff55-411ce2675b0a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[99, 98.7]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Q22) print all prime no. between 1to n\n",
        "n = int(input(\"Enter no:\"))\n",
        "for num in range(2, n+1):\n",
        "   prime = True\n",
        "for i in range(2, num):\n",
        "  if num%i == 0:\n",
        "    prime = False\n",
        "    break\n",
        "    if prime:\n",
        "      print(num)\n"
      ],
      "metadata": {
        "id": "QZXcxx2fZWE8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Q23 WAP to ask the user to enter names of 3 fav movies and store them in a list.\n",
        "a = input(\"enter movie 1 name:\")\n",
        "b = input(\"enter movie 2 name:\")\n",
        "c = input(\"enter movie 3 name:\")\n",
        "d =[a,b,c]\n",
        "e=[]\n",
        "e.append(d)\n",
        "print(e)"
      ],
      "metadata": {
        "id": "H1Hv85RnSkUt",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a4eb4bbc-a63f-4e26-d47c-7d4bb3a475b5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter movie 1 name:avenger \n",
            "enter movie 2 name:lucy\n",
            "enter movie 3 name:pokemon\n",
            "[['avenger ', 'lucy', 'pokemon']]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Q24 WAP to check the list contains a palindrome of elements.[1221,1111,2332] or take input\n",
        "a = []\n",
        "a.append(input(\"enter the element 1:\"))\n",
        "a.append(input(\"enter the element 2:\"))\n",
        "a.append(input(\"enter the element 3:\"))\n",
        "a.append(input(\"enter the element 4:\"))\n",
        "\n",
        "if a[0]==a[0][::-1] and a[1]==a[1][::-1]  and a[2]==a[2][::-1]  and a[3]==a[3][::-1] :\n",
        "  print(\"Palindrome\")\n",
        "else:\n",
        "  print(\"Not palindrome\")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "t_cjNDP1bMUQ",
        "outputId": "4098a0bd-4ed2-4562-ac46-551b13f74a3a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter the element 1:shivjot\n",
            "enter the element 2:shhhs\n",
            "enter the element 3:shshhs\n",
            "enter the element 4:sjjs\n",
            "tojvihs\n",
            "Not palindrome\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Q25 wap to count the number of students with grade 'A' in the following tuple.\n",
        "A = (\"A\",\"C\",\"B\",\"D\",\"A\",\"C\",\"A\")\n",
        "print(A.count(\"A\"))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "g8EA91_usGbN",
        "outputId": "e09760d5-cc45-40a3-85e5-6dca067ef2a4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Q26 wap store the above value in a list & sort them from 'A to D'\n",
        "A = (\"A\",\"C\",\"B\",\"D\",\"A\",\"C\",\"A\")\n",
        "b = list(A)\n",
        "print(b,b.sort())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fzHaLeUeudOP",
        "outputId": "39c98d86-2f08-4b4f-b99c-6b71679332a7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['A', 'A', 'A', 'B', 'C', 'C', 'D'] None\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(b.sort())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "slzOFX3RxC0z",
        "outputId": "04a0a5f4-1ae6-4e58-a8f0-9531c857c080"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "None\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Q27 Dictionary\n",
        "info ={\n",
        "    \"key\":\"value\",\n",
        "    \"name\":\"shivjot\",\n",
        "    1:5.6,\n",
        "    \"list\":[3,\"shivjot\"],\n",
        "    \"tuple\":(\"shivjot\",3,4,),\n",
        "    9.4:\"shivjot\",\n",
        "    (\"shivjot\",55):\"tuple\"\n",
        "}\n",
        "print(info)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "roNeZNQ0xRQA",
        "outputId": "188dcda3-2af0-46ed-864c-4c830cec098a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'key': 'value', 'name': 'shivjot', 1: 5.6, 'list': [3, 'shivjot'], 'tuple': ('shivjot', 3, 4), 9.4: 'shivjot', ('shivjot', 55): 'tuple'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(info[\"list\"])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "z2xJXsrd5Z-Y",
        "outputId": "0d66da82-364b-4e7d-b150-ef3c50d03c29"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[3, 'shivjot']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Q28 change  and new value of name in the above :-\n",
        "info[\"aaa\"]=\"choudhary\"\n",
        "info[\"name\"]=\"niki\"\n",
        "print(info[\"aaa\"])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Rq984BrX6MBd",
        "outputId": "a25256a4-0c62-4ff5-c38f-4c5232cd7ffa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "choudhary\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(info)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "btLWFePx7_Xt",
        "outputId": "b59b20c2-219e-46b5-ab10-4120dd99158c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'key': 'value', 'name': 'niki', 1: 5.6, 'list': [3, 'shivjot'], 'tuple': ('shivjot', 3, 4), 9.4: 'shivjot', ('shivjot', 55): 'tuple', 'aaa': 'choudhary'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Q29 Nested Dictionary\n",
        "dict={\n",
        "    \"name\":\"shivjot\",\n",
        "    \"subject\":{\n",
        "        \"ai/ml\":\"python\",\n",
        "        \"project\":\"OCR APP\"\n",
        "    }\n",
        "}\n",
        "print(dict[\"subject\"][\"project\"])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XZEDlgUtEApK",
        "outputId": "7813658f-ebdc-43fb-822a-339f99aaf94e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "OCR APP\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(dict.keys())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PImXAsRDFSGv",
        "outputId": "1ab78daf-279b-4be0-884d-7f7f47f3d22b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "dict_keys(['name', 'subject'])\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Q30tuple inside a list and list inside a tuple :- list=mutable and tuple = immutable\n",
        "a=[2,3,(4,5,4)]\n",
        "a[2]\n",
        "print(a[-1][0])\n",
        "type(a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XIEnoLAHEjoN",
        "outputId": "d5676823-7c81-4901-d557-a35fa719a2f8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "list"
            ]
          },
          "metadata": {},
          "execution_count": 106
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Q31 Different functions on sets:-\n",
        "a = {\n",
        "    \"name\":\"rahul\",\n",
        "    \"subject\": \"AI/ML\"\n",
        "}\n",
        "# a.clear()\n",
        "# a.get(\"name\")\n",
        "# a.items()\n",
        "# a.keys()\n",
        "# a.values()\n",
        "#a.update({\"Name\":\"shivjot\"})\n",
        "a.update({\"name\":\"goku\"})\n",
        "print(a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "m7wqwaKKGV88",
        "outputId": "e0e3a6bf-a019-48f2-e858-eb9b1db10016"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'name': 'goku', 'subject': 'AI/ML'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Q32 Sets:-\n",
        "a = {\"shivjot\",\"rrr\",\"pokemon\"}\n",
        "# type(a)\n",
        "a.add(\"shiv\")\n",
        "a.remove(\"rrr\")\n",
        "print(a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gikR3Jt3Kjz0",
        "outputId": "b6773e93-e3ed-4248-ab6f-72e822775bdf"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'pokemon', 'shivjot', 'shiv'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Small project:-**"
      ],
      "metadata": {
        "id": "UP-nmOB42O8D"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Q34) Number guessing game using python :)\n",
        "import random\n",
        "print (\"AI Number Guessing Game \")\n",
        "print (\"I am thinking of a number between 1 to 100\")\n",
        "numb = random.randint(1,100)\n",
        "attem = 0\n",
        "while True:\n",
        "  guess = int(input(\"Enter your Guess:-\"))\n",
        "  attem = attem+1\n",
        "  if guess < numb:\n",
        "    print(\"Too low! Try again.\")\n",
        "  elif guess > numb:\n",
        "    print(\"Too high! Try again.\")\n",
        "  else:\n",
        "    print(f\"Correct! The number was {numb}\")\n",
        "    print(f\"You Guessed it in {attem} attempts.\")\n",
        "    break"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uhsWSI7muj6q",
        "outputId": "466ce4fb-b26f-42ff-df98-7504393c7428"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "AI Number Guessing Game \n",
            "I am thinking of a number between 1 to 100\n",
            "Enter your Guess:-50\n",
            "Too high! Try again.\n",
            "Enter your Guess:-40\n",
            "Too low! try again.\n",
            "Enter your Guess:-45\n",
            "Too low! try again.\n",
            "Enter your Guess:-43\n",
            "Too low! try again.\n",
            "Enter your Guess:-44\n",
            "Too low! try again.\n",
            "Enter your Guess:-46\n",
            "Too low! try again.\n",
            "Enter your Guess:-47\n",
            "Too low! try again.\n",
            "Enter your Guess:-48\n",
            "Correct! The number was 48\n",
            "You Guessed it in 8 attempts.\n"
          ]
        }
      ]
    }
  ]
}