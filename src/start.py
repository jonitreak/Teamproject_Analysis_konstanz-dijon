import subprocess

class Start:
    def __init__(self):
        self.available_clients = ["fourier", "multifactor", "data"]

    def run_client(self, client_name):
        """
        Run a specific client based on user input.

        :param client_name: The name of the client to run.
        """
        try:
            if client_name == "fourier":
                subprocess.run(["python", "src\\python_scripts\\frontend\\experimental_frontend.py"], check=True)
            #TODO: Implement other client paths
            # elif client_name == "multifactor":
            #     subprocess.run(["python", ""], check=True)
            # elif client_name == "data":
            #     subprocess.run(["python", ""], check=True)
            else:
                print("Unknown client name. No action taken.")
                quit()
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def get_user_input(self):
        """
        Get user input for selecting a client.
        """
        while True:
            print("Available clients:", self.available_clients)
            client_name = input("Enter the client to run: ")

            if client_name in self.available_clients:
                return client_name
            else:
                print("Invalid client name. Please enter a valid client.")

    def start(self):
        """
        Start the program.
        """
        client_name = self.get_user_input()
        self.run_client(client_name)

# Example usage
if __name__ == "__main__":
    start_instance = Start()
    start_instance.start()
