# This calculator is made by MRayan Asim
from __future__ import annotations


def collatz_steps(n: int) -> int:
    """
    Compute the number of steps for the Collatz sequence starting at *n*
    to reach 1.

    Args:
        n: A positive integer (>= 1).

    Returns:
        Number of steps taken to reach 1.

    Raises:
        ValueError: If n < 1.
    """
    if n < 1:
        raise ValueError(f"n must be a positive integer, got {n!r}")
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps


def _collatz_sequence(n: int) -> list[int]:
    """Return the full Collatz sequence from *n* down to 1 (inclusive)."""
    if n < 1:
        raise ValueError(f"n must be a positive integer, got {n!r}")
    seq: list[int] = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq


def run_gui() -> None:
    """Run the Tkinter GUI for Collatz visualization."""
    import tkinter as tk

    def _calculate_collatz() -> None:
        try:
            number = int(input_entry.get())
            if number < 1:
                raise ValueError
        except ValueError:
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, "Please enter a positive integer.")
            return

        output_text.delete(1.0, tk.END)
        sequence = _collatz_sequence(number)
        for val in sequence:
            output_text.insert(tk.END, str(val) + "\n")

        steps = len(sequence) - 1
        output_text.insert(tk.END, f"\nReached 1 in {steps} steps.")

    window = tk.Tk()
    window.title("Collatz Conjecture by MRayan Asim")
    window.configure(background="black")

    input_label = tk.Label(window, text="Enter a positive integer:", fg="white", bg="black")
    input_label.pack()

    input_entry = tk.Entry(window)
    input_entry.pack()

    calculate_button = tk.Button(
        window, text="Calculate", command=_calculate_collatz, fg="white", bg="dark green"
    )
    calculate_button.pack()

    output_label = tk.Label(window, text="Sequence:", fg="white", bg="black")
    output_label.pack()

    output_frame = tk.Frame(window, bg="black")
    output_frame.pack()

    output_text = tk.Text(output_frame, width=30, height=10, fg="white", bg="black")
    output_text.pack(side=tk.LEFT, fill=tk.Y)

    scrollbar = tk.Scrollbar(output_frame, command=output_text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    output_text.configure(yscrollcommand=scrollbar.set)

    window.mainloop()


if __name__ == "__main__":
    run_gui()
