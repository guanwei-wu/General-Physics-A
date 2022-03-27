{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div id=\"glowscript\" class=\"glowscript\"></div>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "if (typeof Jupyter !== \"undefined\") { window.__context = { glowscript_container: $(\"#glowscript\").removeAttr(\"id\")};}else{ element.textContent = ' ';}"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div id=\"glowscript\" class=\"glowscript\"></div>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "if (typeof Jupyter !== \"undefined\") { window.__context = { glowscript_container: $(\"#glowscript\").removeAttr(\"id\")};}else{ element.textContent = ' ';}"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "if (typeof Jupyter !== \"undefined\") {require.undef(\"nbextensions/vpython_libraries/glow.min\");}else{element.textContent = ' ';}"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "if (typeof Jupyter !== \"undefined\") {require.undef(\"nbextensions/vpython_libraries/glowcomm\");}else{element.textContent = ' ';}"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "if (typeof Jupyter !== \"undefined\") {require.undef(\"nbextensions/vpython_libraries/jquery-ui.custom.min\");}else{element.textContent = ' ';}"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "if (typeof Jupyter !== \"undefined\") {require([\"nbextensions/vpython_libraries/glow.min\"], function(){console.log(\"GLOW LOADED\");});}else{element.textContent = ' ';}"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "if (typeof Jupyter !== \"undefined\") {require([\"nbextensions/vpython_libraries/glowcomm\"], function(){console.log(\"GLOWCOMM LOADED\");});}else{element.textContent = ' ';}"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "if (typeof Jupyter !== \"undefined\") {require([\"nbextensions/vpython_libraries/jquery-ui.custom.min\"], function(){console.log(\"JQUERY LOADED\");});}else{element.textContent = ' ';}"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from vpython import *\n",
    "\n",
    "g = 9.8\t        # g = 9.8 m/s^2\n",
    "size = 0.25     # ball radius = 0.25 m\n",
    "height = 15.0   # ball center initial height = 15 m\n",
    "\n",
    "scene = canvas(width=800, height=800, center=vec(0,height/2,0), background=vec(255, 252, 208)/255.0)  # open a window\n",
    "floor = box(length=30, height=0.01, width=10, color=color.blue)                                       # the floor\n",
    "ball = sphere(radius=size, color=color.red, make_trail=True, trail_radius=0.05)                       # the ball\n",
    "a1 = arrow(color=color.red, shaftwidth=0.05)\n",
    "entirepath = 0\n",
    "displacement = vec(0, 0, 0)\n",
    "timeinair = 0\n",
    "\n",
    "ball.pos = vec(-15, 5, 0)       # ball center initial position\n",
    "ball.v = vec(6, 8, 0)           # ball initial velocity\n",
    "\n",
    "dt = 0.001                      # time step\n",
    "while ball.pos.y >= size:       # until the ball hit the ground\n",
    "    rate(1000)                  # run 1000 times per real second\n",
    "\n",
    "    ball.pos.x = ball.pos.x + ball.v.x*dt\n",
    "    ball.pos.y = ball.pos.y + ball.v.y*dt\n",
    "    ball.v.y = ball.v.y - g*dt\n",
    "    entirepath = entirepath + ((ball.v.x*dt)**2 + (ball.v.y*dt)**2)**0.5\n",
    "    a1.pos = vec(ball.pos.x, ball.pos.y, 0)\n",
    "    a1.axis = vec(ball.v.x, ball.v.y, 0)\n",
    "    timeinair = timeinair + 0.001\n",
    "    \n",
    "displacement = vec(ball.pos)-vec(-15,5,0)\n",
    "msg = text(text='the velocity vector ='+str(ball.v), pos=vec(-10,-6,0))\n",
    "msg = text(text='the displacement ='+str(displacement), pos=vec(-10,-9,0))\n",
    "msg = text(text='the entire path ='+str(entirepath), pos=vec(-10,-12,0))\n",
    "msg = text(text='the time in th air ='+str(timeinair), pos=vec(-10,-15,0))"
   ]
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
