**Logistic Regression**

**Q1**

Suppose that you have trained a logistic regression classifier, and it outputs on a new example x a prediction hθ(x) = 0.7. This means (check all that apply):
- [ ] Our estimate for P(y=0|x;\theta)P(y=0∣x;θ) is 0.7.
- [x] Our estimate for P(y=1|x;\theta)P(y=1∣x;θ) is 0.7.
- [x] Our estimate for P(y=0|x;\theta)P(y=0∣x;θ) is 0.3.
- [ ] Our estimate for P(y=1|x;\theta)P(y=1∣x;θ) is 0.3.


**Q2**

<img width="327" alt="2" src="https://user-images.githubusercontent.com/38349049/46675807-8982db00-cbdf-11e8-93f3-fa9f83cd7e2b.png">
<img width="354" alt="2a" src="https://user-images.githubusercontent.com/38349049/46675808-8982db00-cbdf-11e8-8d5c-5bb5a02ef82a.png">

- [x] answer1
- [ ] 2
- [ ] 3
- [ ] 4 - If we train gradient descent for enough iterations, for some examples x^(i) in the training set it is possible to obtain hθ(x(i))>1.
- [x] 5 - J(θ) will be a convex function, so gradient descent should converge to the global minimum.

**Q3**

For logistic regression, the gradient is given by J(θ)=m1∑i=1m(hθ(x(i))−y(i))xj(i). Which of these is a correct gradient descent update for logistic regression with a learning rate of α? Check all that apply.

- [ ] θj:=θj−αm1∑i=1m(θTx−y(i))xj(i) (simultaneously update for all jj).
- [x] θ:=θ−αm1∑i=1m((1/1+e^(−θTx^(i)))−y(i))x(i).
- [ ] θ:=θ−αm1∑i=1m(θTx−y(i))x(i).
- [ ] θ:=θ−αm1∑i=1m(hθ(x(i))−y(i))x(i).
...
<img width="454" alt="zrzut ekranu 2018-10-09 17 03 31" src="https://user-images.githubusercontent.com/38349049/46678768-9f939a00-cbe5-11e8-919d-9bfeffe46d71.png">

**Q4**

Which of the following statements are true? Check all that apply.
- [x] The cost function J(θ) for logistic regression trained with m≥1 examples is always greater than or equal to zero.
- [x] The sigmoid function  g(z)=1/1+e^−z is never greater than one (>1).
- [ ] For logistic regression, sometimes gradient descent will converge to a local minimum (and fail to find the global minimum). This is the reason we prefer more advanced optimization algorithms such as fminunc (conjugate gradient/BFGS/L-BFGS/etc).
- [ ] Linear regression always works well for classification if you classify by using a threshold on the prediction made by linear regression.
...
<img width="439" alt="zrzut ekranu 2018-10-09 17 03 17" src="https://user-images.githubusercontent.com/38349049/46678769-9f939a00-cbe5-11e8-9e45-00c3a709f55b.png">

**Q5**
Suppose you train a logistic classifier hθ(x)=g(θ0+θ1x1+θ2x2). Suppose θ0=−6,θ1=1,θ2=0. Which of the following figures represents the decision boundary found by your classifier?

<img width="225" alt="3" src="https://user-images.githubusercontent.com/38349049/46675809-8982db00-cbdf-11e8-811c-5a34db648039.png">
<img width="208" alt="3a" src="https://user-images.githubusercontent.com/38349049/46675810-8982db00-cbdf-11e8-8133-10d09cdaa21c.png">
