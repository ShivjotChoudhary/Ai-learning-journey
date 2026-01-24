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
        "<a href=\"https://colab.research.google.com/github/ShivjotChoudhary/ai-learning-journey/blob/main/day-06-loops-practice.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "PsQ9w-OQmTNQ"
      },
      "outputs": [],
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
        "id": "pdeynL0nnjqm"
      },
      "execution_count": null,
      "outputs": []
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
        "id": "3Vcrjrb7rIyJ"
      },
      "execution_count": null,
      "outputs": []
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
        "id": "HuvbyP3ArIvB"
      },
      "execution_count": null,
      "outputs": []
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
        "id": "5ZLryWoKrIsJ"
      },
      "execution_count": null,
      "outputs": []
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
        "id": "MDxVfAAcrIpk"
      },
      "execution_count": null,
      "outputs": []
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
        "id": "rVJTUQ-rrIm8"
      },
      "execution_count": null,
      "outputs": []
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
        "id": "FaE2bV1irIkE"
      },
      "execution_count": null,
      "outputs": []
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
        "id": "NBfiDMhUrIhd"
      },
      "execution_count": null,
      "outputs": []
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
        "id": "XC6a9qYtrIe3"
      },
      "execution_count": null,
      "outputs": []
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
        "id": "MEzu2q_orIb_"
      },
      "execution_count": null,
      "outputs": []
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
        "id": "rYAXnsqVn-9c"
      },
      "execution_count": null,
      "outputs": []
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
        "id": "IGvDVbi_qtvR"
      },
      "execution_count": null,
      "outputs": []
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
        "id": "2Q7FpZj_tZhx"
      },
      "execution_count": null,
      "outputs": []
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
        "id": "YXM7D6HnwQ6l"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Q14 indexing\n",
        "a = \"shivjot\"\n",
        "print(\"->\",a[4],\"\\n\",a[0:4])"
      ],
      "metadata": {
        "id": "jxxHD31CTmLE"
      },
      "execution_count": null,
      "outputs": []
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
        "id": "k--XJEtJTnZe"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# q16 minus indexing :-\n",
        "a= \"apple\"\n",
        "print(a[-2:])"
      ],
      "metadata": {
        "id": "QxTAYQ_ErceY"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Q17 using .endswith(\"\")#returns boolean value\n",
        "str=\"shivjot\"\n",
        "print(str.endswith(\"ot\"))  #str.endswith(\"\") returns true if string ends with substr"
      ],
      "metadata": {
        "id": "aJrm-dOYu-ig"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#q18 using capitalize () function #it capitalizes the first  index.\n",
        "a=\"shivjot\"\n",
        "print(a.capitalize())"
      ],
      "metadata": {
        "id": "R_Gh_wxdwyJJ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#q19 using replace(\"\")\n",
        "a=\"clock\"\n",
        "print(a.replace(\"loc\",\"oo\"))"
      ],
      "metadata": {
        "id": "34yXW6bcyBeH"
      },
      "execution_count": null,
      "outputs": []
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
        "id": "RBXZ7CM76S0A"
      },
      "execution_count": null,
      "outputs": []
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
        "id": "dNZU6t-cOzim"
      },
      "execution_count": null,
      "outputs": []
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
        "id": "H1Hv85RnSkUt"
      },
      "execution_count": null,
      "outputs": []
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
        "id": "t_cjNDP1bMUQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Q25 wap to count the number of students with grade 'A' in the following tuple.\n",
        "A = (\"A\",\"C\",\"B\",\"D\",\"A\",\"C\",\"A\")\n",
        "print(A.count(\"A\"))"
      ],
      "metadata": {
        "id": "g8EA91_usGbN"
      },
      "execution_count": null,
      "outputs": []
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
        "id": "fzHaLeUeudOP"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(b.sort())"
      ],
      "metadata": {
        "id": "slzOFX3RxC0z"
      },
      "execution_count": null,
      "outputs": []
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
        "id": "roNeZNQ0xRQA"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(info[\"list\"])"
      ],
      "metadata": {
        "id": "z2xJXsrd5Z-Y"
      },
      "execution_count": null,
      "outputs": []
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
        "id": "Rq984BrX6MBd"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(info)"
      ],
      "metadata": {
        "id": "btLWFePx7_Xt"
      },
      "execution_count": null,
      "outputs": []
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
        "id": "XZEDlgUtEApK"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(dict.keys())"
      ],
      "metadata": {
        "id": "PImXAsRDFSGv"
      },
      "execution_count": null,
      "outputs": []
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
        "id": "XIEnoLAHEjoN"
      },
      "execution_count": null,
      "outputs": []
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
        "id": "m7wqwaKKGV88"
      },
      "execution_count": null,
      "outputs": []
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
        "id": "gikR3Jt3Kjz0"
      },
      "execution_count": null,
      "outputs": []
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
        "id": "uhsWSI7muj6q"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#hiiii"
      ],
      "metadata": {
        "id": "ZtQeXkPGVw-A"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "%cd /content/ai-learning-journey\n",
        "!git pull\n",
        "#Practice Python\n",
        "\n",
        "!git add .\n",
        "!git commit -m \"Day 3: loops practice\"   # change message daily\n",
        "!git push\n"
      ],
      "metadata": {
        "id": "bgE6NWaXV725"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#hello"
      ],
      "metadata": {
        "id": "KBJ4A5QAWMkK"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "!git add .\n",
        "!git commit -m \"Day 4: loops practice\" # change message daily\n",
        "!git push"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "G7XBUEkxWPXk",
        "outputId": "84d94abf-f0c5-4161-bff9-4f51167e041c"
      },
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "On branch main\n",
            "Your branch is up to date with 'origin/main'.\n",
            "\n",
            "nothing to commit, working tree clean\n",
            "Everything up-to-date\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/ai-learning-journey\n",
        "!git pull\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4AhVGb00XS5b",
        "outputId": "c1593e28-aea1-43ae-e1d8-6b6cde8b88a5"
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/ai-learning-journey\n",
            "Already up to date.\n"
          ]
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
        "a.update({\"name\":\"goku\"})\n",
        "print(a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DIH3y_YaXUIn",
        "outputId": "60e25400-5b50-42be-9e88-c9048b5bb5c2"
      },
      "execution_count": 36,
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
        "!git add .\n",
        "!git commit -m \"Day 4: loops practice\"\n",
        "!git push\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JtgUqV3KXbGd",
        "outputId": "8b818e51-749e-4eba-8feb-27de149f8c9b"
      },
      "execution_count": 40,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "On branch main\n",
            "Your branch is up to date with 'origin/main'.\n",
            "\n",
            "nothing to commit, working tree clean\n",
            "Everything up-to-date\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "code = \"\"\"\n",
        "# Day 4 - Loops Practice\n",
        "\n",
        "print(\"Numbers 1 to 10:\")\n",
        "for i in range(1, 11):\n",
        "    print(i)\n",
        "\n",
        "print(\"\\\\nSum of 1 to 100:\")\n",
        "total = sum(range(1, 101))\n",
        "print(total)\n",
        "\n",
        "print(\"\\\\nFactorial of 5:\")\n",
        "fact = 1\n",
        "for i in range(1, 6):\n",
        "    fact *= i\n",
        "print(fact)\n",
        "\"\"\"\n",
        "\n",
        "with open(\"/content/ai-learning-journey/day-04-loops.py\", \"w\") as f:\n",
        "    f.write(code)\n",
        "\n",
        "print(\"Saved day-04-loops.py successfully!\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bFu6fQmqYedq",
        "outputId": "0bef8bab-a4df-4c89-87f3-302f1ed04307"
      },
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saved day-04-loops.py successfully!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/ai-learning-journey\n",
        "!git add .\n",
        "!git commit -m \"Day 4: loops practice\"\n",
        "!git push"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mI25bubyYity",
        "outputId": "7f5ccda8-6835-4087-c162-b80b989db14d"
      },
      "execution_count": 43,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/ai-learning-journey\n",
            "[main d9af4ae] Day 4: loops practice\n",
            " 1 file changed, 16 insertions(+)\n",
            " create mode 100644 day-04-loops.py\n",
            "Enumerating objects: 4, done.\n",
            "Counting objects: 100% (4/4), done.\n",
            "Delta compression using up to 2 threads\n",
            "Compressing objects: 100% (3/3), done.\n",
            "Writing objects: 100% (3/3), 442 bytes | 442.00 KiB/s, done.\n",
            "Total 3 (delta 1), reused 0 (delta 0), pack-reused 0\n",
            "remote: Resolving deltas: 100% (1/1), completed with 1 local object.\u001b[K\n",
            "To https://github.com/ShivjotChoudhary/ai-learning-journey.git\n",
            "   dc1eb28..d9af4ae  main -> main\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git config --global credential.helper store"
      ],
      "metadata": {
        "id": "_ucUchkpaMRf"
      },
      "execution_count": 45,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!git push\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c4F2e6tZaRbt",
        "outputId": "123f7f51-8ad5-4419-9d9f-33bf9319b6cc"
      },
      "execution_count": 47,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "remote: Invalid username or token. Password authentication is not supported for Git operations.\n",
            "fatal: Authentication failed for 'https://github.com/ShivjotChoudhary/ai-learning-journey.git/'\n"
          ]
        }
      ]
    }
  ]
}