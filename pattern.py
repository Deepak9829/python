{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " *** \n",
      "*   *\n",
      "*   *\n",
      "*****\n",
      "*   *\n",
      "*   *\n",
      "*   *\n"
     ]
    }
   ],
   "source": [
    "for row in range(0,7):\n",
    "    for col in range(0,5):\n",
    "        if ((col==0 or col==4) and (row!=0) or (row==0 or row==3) and (col>0 and\n",
    "                                                                       col<4)):\n",
    "            print(\"*\",end=\"\")\n",
    "    \n",
    "        else:\n",
    "             print(end=\" \")\n",
    "            \n",
    "    print()            \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a number5\n",
      "5 x 1 = 5\n",
      "5 6\n",
      "1\n",
      "5 x 2 = 10\n",
      "5 6\n",
      "2\n",
      "5 x 3 = 15\n",
      "5 6\n",
      "3\n",
      "5 x 4 = 20\n",
      "5 6\n",
      "4\n",
      "5 x 5 = 25\n",
      "5 6\n",
      "5\n",
      "5 x 6 = 30\n",
      "5 6\n",
      "6\n",
      "5 x 7 = 35\n",
      "5 6\n",
      "7\n",
      "5 x 8 = 40\n",
      "5 6\n",
      "8\n",
      "5 x 9 = 45\n",
      "5 6\n",
      "9\n"
     ]
    }
   ],
   "source": [
    "num=int(input(\"enter a number\"))\n",
    "for i in range(1,10):\n",
    "    print(num,'x',i,'=',num*i)\n",
    "    print(num,(num+1))\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " *** \n",
      "*   *\n",
      "*   *\n",
      "*****\n",
      "*   *\n",
      "*   *\n",
      " *** \n"
     ]
    }
   ],
   "source": [
    "for row in range(0,7):\n",
    "    for col in range(0,5):\n",
    "        if((col==0 or col==4 ) and (row!=0 and row!=6) or (row==0 or row==3 or row==6)\n",
    "           and(col>0 and col<4)):\n",
    "            print(\"*\",end=\"\")\n",
    "        else:\n",
    "            print(end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " *** \n",
      "*    \n",
      "*    \n",
      "*    \n",
      "*    \n",
      "*    \n",
      " *** \n"
     ]
    }
   ],
   "source": [
    "for row in range(0,7):\n",
    "    for col in range(0,5):\n",
    "        if((col==0 ) and (row!=0 and row!=6) or (row==0 or row==6)\n",
    "           and(col>0 and col<4)):\n",
    "            print(\"*\",end=\"\")\n",
    "        else:\n",
    "            print(end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " *** \n",
      "  * *\n",
      "  * *\n",
      "  * *\n",
      "  * *\n",
      "  * *\n",
      " *** \n"
     ]
    }
   ],
   "source": [
    "for row in range(0,7):\n",
    "    for col in range(0,5):\n",
    "        if((col==4 or col==2) and (row!=0 and row!=6) or (row==0 or row==6)\n",
    "           and(col>0 and col<4)):\n",
    "            print(\"*\",end=\"\")\n",
    "        else:\n",
    "            print(end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " *** \n",
      "*    \n",
      "*    \n",
      "**** \n",
      "*    \n",
      "*    \n",
      " *** \n"
     ]
    }
   ],
   "source": [
    "for row in range(0,7):\n",
    "    for col in range(0,5):\n",
    "        if((col==0 ) and (row!=0 and row!=6) or (row==0 or row==6 or row==3)\n",
    "           and(col>0 and col<4)):\n",
    "            print(\"*\",end=\"\")\n",
    "        else:\n",
    "            print(end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "**** \n",
      "*    \n",
      "*    \n",
      "**** \n",
      "*    \n",
      "*    \n",
      "*    \n"
     ]
    }
   ],
   "source": [
    "for row in range(0,7):\n",
    "    for col in range(0,5):\n",
    "        if((col==0 )  or (row==0 or row==3)\n",
    "           and(col>0 and col<4)):\n",
    "            print(\"*\",end=\"\")\n",
    "        else:\n",
    "            print(end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*****   \n",
      "*       \n",
      "****    \n",
      "*  ***  \n",
      "*****   \n",
      "*   *   \n",
      "*   *   \n",
      "*   *   \n"
     ]
    }
   ],
   "source": [
    "for row in range(0,8):\n",
    "    for col in range(0,8):\n",
    "        if((col==0) or (col==4 and (row!=1 and row!=2)) or (row==0 or row==2 or row==4)\n",
    "           and(col>0 and col<4)) or (row==3 and (col==3 or col==5)):\n",
    "            print(\"*\",end=\"\")\n",
    "        else:\n",
    "            print(end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*   *\n",
      "*   *\n",
      "*   *\n",
      "*****\n",
      "*   *\n",
      "*   *\n",
      "*   *\n"
     ]
    }
   ],
   "source": [
    "for row in range(0,7):\n",
    "    for col in range(0,5):\n",
    "        if((col==0 or col==4)  or (row==3)\n",
    "           and(col>0 and col<4)):\n",
    "            print(\"*\",end=\"\")\n",
    "        else:\n",
    "            print(end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " *** \n",
      "  *  \n",
      "  *  \n",
      "  *  \n",
      "  *  \n",
      "  *  \n",
      " *** \n"
     ]
    }
   ],
   "source": [
    "for row in range(0,7):\n",
    "    for col in range(0,5):\n",
    "        if((col==2) or (row==0 or row==6)\n",
    "           and(col>0 and col<4)):\n",
    "            print(\"*\",end=\"\")\n",
    "        else:\n",
    "            print(end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "******\n",
      "   *  \n",
      "   *  \n",
      "   *  \n",
      "   *  \n",
      "*  *  \n",
      "****  \n"
     ]
    }
   ],
   "source": [
    "for row in range(0,7):\n",
    "    for col in range(0,6):\n",
    "        if(( col==3) or (col==0 and(row!=1 and row!=2 and row!=3 and row!=4)) or\n",
    "           (row==0 or row==6  and (col!=3 and col!=4 and col!=5))\n",
    "           and(col>0 and col<6)):\n",
    "            print(\"*\",end=\"\")\n",
    "        else:\n",
    "            print(end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*  *\n",
      "* * \n",
      "**  \n",
      "*   \n",
      "**  \n",
      "* * \n",
      "*  *\n"
     ]
    }
   ],
   "source": [
    "for row in range(0,7):\n",
    "    for col in range(0,4):\n",
    "        if((col==0 ) or(row==0 and ( col!=1 and col!=2)) \n",
    "           or (row==1 and (col!=1 and col!=3)) or (row==2 and \n",
    "                                                   (col!=2 and col!=3)) or (row==4 and (col!=2 and col!=3)) or\n",
    "          (row==5 and(col!=1 and col!=3)) or (row==6 and (col!=1 and col!=2))):\n",
    "            print(\"*\",end=\"\")\n",
    "        else:\n",
    "            print(end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*   \n",
      "*   \n",
      "*   \n",
      "*   \n",
      "*   \n",
      "*   \n",
      "****\n"
     ]
    }
   ],
   "source": [
    "for row in range(0,7):\n",
    "    for col in range(0,4):\n",
    "        if((col==0) or (row==6)\n",
    "           and(col>0 and col<4)):\n",
    "            print(\"*\",end=\"\")\n",
    "        else:\n",
    "            print(end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*       *\n",
      "**     **\n",
      "* *   * *\n",
      "*  * *  *\n",
      "*   *   *\n",
      "*       *\n",
      "*       *\n",
      "*       *\n"
     ]
    }
   ],
   "source": [
    "for row in range(0,8):\n",
    "    for col in range(0,9):\n",
    "        if((col==0 or col==8) or (row==1 and (col!=2 and col!=3 and col!=4 and\n",
    "                                             col!=5 and col!=6)) or (row==2 and (\n",
    "        col!=1 and col!=3 and col!=4 and col!=5 and col!=7)) or\n",
    "                                 (row==3 and ( col!=1 and col!=2 and col!=4 and\n",
    "                                             col!=6 and col!=7)) or (row==4 and(\n",
    "                                 col!=1 and col!=2 and col!=3 and col!=5 and\n",
    "                                 col!=6 and col!=7))\n",
    "           and(col>0 and col<9)):\n",
    "            print(\"*\",end=\"\")\n",
    "        else:\n",
    "            print(end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*     *\n",
      "**    *\n",
      "* *   *\n",
      "*  *  *\n",
      "*   * *\n",
      "*    **\n",
      "*     *\n"
     ]
    }
   ],
   "source": [
    "for row in range(0,7):\n",
    "    for col in range(0,7):\n",
    "        if((col==0 or col==6) or (row==1 and ( col!=2 and col!=3 and col!=4 and\n",
    "                                             col!=5)) or (row==2 and(col!=1 and\n",
    "                                                                    col!=3 and \n",
    "                                                                    col!=4 and\n",
    "                                                                    col!=5))\n",
    "           or(row==3 and (col!=1 and col!=2 and col!=4 and col!=5)) or \n",
    "           (row==4 and (col!=1 and col!=2 and col!=3 and col!=5)) or\n",
    "           (row==5 and(col!=1 and col!=2 and col!=3 and col!=4))\n",
    "           and(col>0 and col<7)):\n",
    "            print(\"*\",end=\"\")\n",
    "        else:\n",
    "            print(end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "**** \n",
      "*   *\n",
      "*   *\n",
      "**** \n",
      "*    \n",
      "*    \n",
      "*    \n"
     ]
    }
   ],
   "source": [
    "for row in range(0,7):\n",
    "    for col in range(0,5):\n",
    "        if col==0 or (col==4 and (row==1 or row==2) or (row==0 or row==3) and(col>0 and col<4)):\n",
    "            print(\"*\",end=\"\")\n",
    "        else:\n",
    "            print(end=\" \")\n",
    "    print()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "******\n",
      "   *  \n",
      "   *  \n",
      "   *  \n",
      "   *  \n",
      "*  *  \n",
      "****  \n"
     ]
    }
   ],
   "source": [
    "for row in range(0,7):\n",
    "    for col in range(0,6):\n",
    "        if( ( col==3) or (col==0 and(row!=1 and row!=2 and row!=3 and row!=4)) or\n",
    "           (row==0 or row==6  and (col!=3 and col!=4 and col!=5))\n",
    "           and(col>0 and col<6)):\n",
    "            print(\"*\",end=\"\")\n",
    "        else:\n",
    "            print(end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "***************"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
