#!/usr/bin/python3
import matplotlib.pyplot as plt

def nrz_encoding(binary_str):
    signal = []
    for bit in binary_str:
        if bit == '1':
            signal.append(1)
        else:
            signal.append(0)
    return signal

def rz_encoding(binary_str):
    signal = []
    for bit in binary_str:
        if bit == '1':
            signal.extend([1, 0])
        else:
            signal.extend([-1, 0])
    return signal

def manchester_encoding(binary_str):
    signal = []
    for bit in binary_str:
        if bit == '1':
            signal.extend([-1, 1])
        else:
            signal.extend([1, -1])
    return signal

def differential_manchester_encoding(binary_str):
    signal = []

    curr_sig = [1, -1]
    for bit in binary_str:
        if bit == '1':
            signal.extend(curr_sig)
        else:
            curr_sig.reverse()
            signal.extend(curr_sig)
        curr_sig.reverse()
            
    return signal


def plot_signal(signal, title, binary_str):
    plt.figure(figsize=(10, 4))
    plt.step(range(len(signal)), signal, where='post', linestyle='-', color='b')

    bit_width = len(signal) / len(binary_str)
    for i, bit in enumerate(binary_str):
        x_position = (i * bit_width) + bit_width / 2 
        plt.text(x_position, 1.2, bit, fontsize=12, ha='center', color='red')
    
        #Draw a vertical line to separate each bit visually
        plt.axvline((i+1) * bit_width, color='black', linestyle='--', linewidth=0.9)
    
    # Add horizontal line at y=0 (on the x-axis)
    plt.axhline(0, color='black', linewidth=1, linestyle='-')  # This adds the horizontal line at y=0

    plt.title(title)
    plt.ylim(-1.5, 1.5)
    plt.xlim(0, len(signal))
    plt.ylabel('Signal Amplitude')
    plt.xlabel('Time')
    plt.grid(True)
    plt.show()

def get_binary_input():
    while True:
        binary_str = input("Enter the binary string (0s and 1s only): ").strip()
        if not binary_str:
            print("Error: Input cannot be empty.\n")
            continue
        if not all(bit in '01' for bit in binary_str):
            print("Error: The input must contain only 0s and 1s.\n")
            continue
        return binary_str

def main():
    while (True):
        binary_str = get_binary_input()

        print("\nSelect the encoding scheme:")
        print("1. NRZ")
        print("2. RZ")
        print("3. Manchester")
        print("4. Differential Manchester")

        while(True):
            choice = input("Enter the number of the encoding scheme: ").strip()

            if choice == '1':
                signal = nrz_encoding(binary_str)
                plot_signal(signal, "NRZ Encoding", binary_str)
            elif choice == '2':
                signal = rz_encoding(binary_str)
                plot_signal(signal, "RZ Encoding", binary_str)
            elif choice == '3':
                signal = manchester_encoding(binary_str)
                plot_signal(signal, "Manchester Encoding", binary_str)
            elif choice == '4':
                signal = differential_manchester_encoding(binary_str)
                plot_signal(signal, "Differential Manchester", binary_str)
            else:
                print("Invalid choice!")
            
            another_scheme = input("\n- Applying another scheme? Y/N ")
            if(another_scheme.lower() == 'n'):
                break
        
        another_simulation = input("\n- Making another simulation? Y/N  ")
        if (another_simulation.lower() == 'n'):
            break
    
if __name__ == "__main__":
    main()