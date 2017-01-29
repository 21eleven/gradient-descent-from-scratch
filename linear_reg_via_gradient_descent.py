from numpy import *

def find_error(b, m, pts):
    totalErr = 0

    for i in range(0, len(pts)):
        x, y = pts[i, 0], pts[i, 1]
        totalErr += (y - (m * x + b)) ** 2

    return totalErr / float(len(pts))

def step_gradient(b, m, pts, learning_rate):
    
    b_gradient = []
    m_gradient = []
    N = float(len(pts))
    
    for i in range(0, int(N)):
        
        x, y = pts[i, 0], pts[i, 1]
        
        b_gradient.append(-(2/N) * (y - ((m * x) + b)))
        m_gradient.append(-(2/N) * x * (y - ((m * x) + b)))


    new_b = b - (learning_rate * sum(b_gradient))
    new_m = m - (learning_rate * sum(m_gradient))

    print new_b, new_m

    return [new_b, new_m]

def gradient_descent(pts, b, m, learning_rate, n_iterations):

    for i in range(n_iterations):
        b, m = step_gradient(b, m , array(pts), learning_rate)

    return [b, m]


def run():
    
    pts = genfromtxt("data.csv", delimiter=",")
    
    #hyper parameters
    learning_rate = 0.0001
    b_0 = 0 #initial y intercept
    m_0 = 0 # initial slop
    n_iterations = 1000
    
    print "Running..."
    [b, m] = gradient_descent(pts, b_0, m_0, learning_rate, n_iterations)
    print "After {} iterations b = {}, m = {}, error = {}".format(n_iterations,b,m,find_error(b, m, pts))

if __name__ == '__main__':
    run()
