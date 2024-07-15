# Apache Airflow CLI :
# Run the command below in the terminal to list all the existing DAGs:
airflow dags list


# Run the command below in the terminal to list all tasks in the DAG named example_bash_operator:
airflow tasks list example_bash_operator


# Run a command to list all tasks for the DAG named tutorial:
airflow tasks list tutorial


# Run the command below in the terminal to unpause a DAG named tutorial:
airflow dags unpause tutorial


# Run a command to unpause the DAG named example_branch_operator:
airflow dags unpause example_branch_operator


# List tasks for the DAG example_branch_labels:
airflow tasks list example_branch_labels


# Unpause the DAG example_branch_labels:
airflow dags unpause example_branch_labels


# Pause the DAG example_branch_labels:
airflow dags pause example_branch_labels