**Question 1**
Consider the problem of predicting how well a student does in her second year of college/university, given how well she did in her first year.
Specifically, let x be equal to the number of "A" grades (including A-. A and A+ grades) that a student receives in their first year of college (freshmen year). We would like to predict the value of y, which we define as the number of "A" grades they get in their second year (sophomore year).
Here each row is one training example. Recall that in linear regression, our hypothesis is hθ(x)=θ0+θ1x, and we use m to denote the number of training examples.

x | y
-- | --
0 | 1
2 | 1
4 | 3
3 | 4

For the training set given above (note that this training set may also be referenced in other questions in this quiz), what is the value of m? In the box below, please enter your answer (which should be a number between 0 and 10).

m = **4**

**Q2**
For this question, assume that we are using the training set from Q1. Recall our definition of the construction was:
J(θ0,θ1)=1/2m sum(hθ(x^(i))-y^(i))^2.
What is J(θ0,θ1)?

Answer: **0.5**
**WHY?**: J(θ1)=J(1)=1/2m[(1-0)^2+(1-2)^2+(3-4)^+(4-3)^2]=1/8[4]=0.5

**Q3**
Suppose we set θ0=-1, θ1=0.5. What is hθ(4)?

hθ(x)=θ0+θ1x
hθ(4)=(-1)+0.5x=**1**

**Q4**
Answers:
- **If we start from point B, gradient descent with a well-chosen learning rate will eventually help us reach at or near point A, as the value of cost function J(θ0,θ1) is minimum at A.**
- **Point P (the global minimum of plot 2) corresponds to point A of Plot 1.**

**Q5**
Suppose that for some linear regression problem (say, predicting housing prices as in the lecture), we have some training set, and for our training set we managed to find some θ0, θ1 such that J(θ0,θ1)=0.
Which of the statements below must then be true? (Check all that apply.)
- For this to be true, we must have y(i)=0 for every value of i=1,2,…,m.
- Gradient descent is likely to get stuck at a local minimum and fail to find the global minimum.
- For this to be true, we must have θ0=0 and θ1=0 so that hθ(x)=0. - they dont need to be both=0
- **Our training set can be fit perfectly by a straight line, i.e., all of our training examples lie perfectly on some straight line.**

