import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def main():
    '''
    Calculates P(x<1|N(0,1)) and P(x>μ+2σ|N(175, 3)) and displays both the PDF and CDF
    for each case.
    '''

    # Part 1. P(x < 1 | N(0,1))
    mu_a, sig_a = 0, 1
    c_a = 1
    p_a = norm.cdf(c_a, mu_a, sig_a)

    # Generate data for plots
    x_a = np.linspace(mu_a - 5 * sig_a, mu_a + 5 * sig_a, 500)
    cdf_a = norm.cdf(x_a, mu_a, sig_a)
    pdf_a = norm.pdf(x_a, mu_a, sig_a)

    # Build the plots for Part 1
    plt.subplots(2, 1, sharex=True)
    plt.subplot(2, 1, 1)
    plt.plot(x_a, pdf_a)
    plt.xlim(x_a.min(), x_a.max())
    plt.ylim(0, pdf_a.max() * 1.1)

    x_fill = np.linspace(mu_a - 5 * sig_a, c_a, 100)
    pdf_fill = norm.pdf(x_fill, mu_a, sig_a)
    ax = plt.gca()
    ax.fill_between(x_fill, pdf_fill, color='grey', alpha=0.3)

    plt.ylabel('f(x)', size=12)
    plt.title('Part 1: P(x<1|N(0,1))')

    plt.subplot(2, 1, 2)
    plt.plot(x_a, cdf_a)
    plt.ylim(0, 1)
    plt.ylabel(r'$\Phi(x)$', size=12)
    plt.xlabel('x')
    plt.plot(c_a, p_a, 'o', markerfacecolor='white', markeredgecolor='red')

    # Part 2. P(x > μ + 2σ | N(175, 3))
    mu_b, sig_b = 175, 3
    c_b = mu_b + 2 * sig_b
    p_b = 1 - norm.cdf(c_b, mu_b, sig_b)  # For P(x > μ + 2σ)

    x_b = np.linspace(mu_b - 5 * sig_b, mu_b + 5 * sig_b, 500)
    cdf_b = norm.cdf(x_b, mu_b, sig_b)
    pdf_b = norm.pdf(x_b, mu_b, sig_b)

    # Build the plots for Part 2
    plt.subplots(2, 1, sharex=True)
    plt.subplot(2, 1, 1)
    plt.plot(x_b, pdf_b)
    plt.xlim(x_b.min(), x_b.max())
    plt.ylim(0, pdf_b.max() * 1.1)

    x_fill = np.linspace(c_b, mu_b + 5 * sig_b, 100)
    pdf_fill = norm.pdf(x_fill, mu_b, sig_b)
    ax = plt.gca()
    ax.fill_between(x_fill, pdf_fill, color='grey', alpha=0.3)

    plt.ylabel('f(x)', size=12)
    plt.title('Part 2: P(x>μ+2σ|N(175,3))')

    plt.subplot(2, 1, 2)
    plt.plot(x_b, cdf_b)
    plt.ylim(0, 1)
    plt.ylabel(r'$\Phi(x)$', size=12)
    plt.xlabel('x')
    plt.plot(c_b, 1 - p_b, 'o', markerfacecolor='white', markeredgecolor='red')

    plt.show()

if __name__ == "__main__":
    main()


