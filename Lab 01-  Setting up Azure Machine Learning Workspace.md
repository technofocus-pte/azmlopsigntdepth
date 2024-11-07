### **Implementing Machine Leaning and MLOps for Targeted custmer marketing with Azure Machine Learning**

#### **Introduction**
Contoso Bank is undergoing a comprehensive digital transformation across all its departments to enhance their operational efficiency and customer engagement. Currently, the bank's customer base is predominantly composed of liability customers (depositors), while the asset customer base (borrowers) is relatively smaller. The bank aims to rapidly expand its asset customer segment to generate additional revenue through loan interests.

In the previous quarter, the bank launched a marketing campaign targeting potential borrowers, which resulted in an average conversion rate in the single digits. As part of its digital transformation strategy, the marketing department seeks to design more effective campaigns that leverage targeted marketing techniques. The goal is to significantly increase the conversion ratio to double digits while maintaining the same budget as the last campaign. This initiative is pivotal for driving growth and maximizing the bank's profitability through increased borrowing activity.

**Workshop Objective**

Contoso Bank's marketing team would like to build a Proof of Concept (POC) as part of which they'd need to work with the Data Analytics and AI engineering teams within Contoso IT team, tp build an app that uses data-driven, AI-enhanced strategies to improve campaign targeting, so the marketing team can aim for a double-digit conversion rate of the asset customer base within the same budget.
In this lab, you will work as an AI app developer in Contoso Bank's AI engineering team to build a sample app, which makes use of Azure AI, AML and MLOps capabilities to achieve the solution.

**Tools and Technologies used in this workshop :**

**Azure Machine Learning (AML)**: For building, training, and
    deploying the predictive model in the banking scenario.

**MLOps**: For covering model training, deployment, and automated model
    management.

**Azure AI Studio**: Used to create, configure, and deploy the
    chatbot powered by Azure AI and integrated with the AML model.

**Azure AI Search**: For enriching the chatbot with search and query
    capabilities based on customer data and loan details.

**Azure App Service**: To host and manage the deployed web
    application (chat app).

**Azure Blob Storage**: For storing and managing datasets used in
    training and prediction.

**Python SDK**: For interacting with Azure services, building the
    model and working with data pipelines.

### Lab 01: Setting up Azure Machine Learning Workspace
#### **Introduction:**
In this exercise, we will set up the foundational components of the Azure Machine Learning workspace. This workspace will provide an environment where we train, deploy, and manage machine learning models. The tasks involves creating a new Azure Machine Learning resource, configuring the necessary compute resources, and ensuring that all security and access controls are in place. This environment will serve as the backbone for building predictive models and integrating MLOps into Contoso Bank’s marketing strategies. We are also assigning required permissions to the subscription to perform the above tasks and uploading loan guide documents for chatapp to use and respond to customer queries

**In this lab you will learn how-to:**

- Setup Azure Machine Learning workspace

### **Task 1: Setting up Azure Machine Learning Workspace** 

#### **Introduction:**
>In this task, we will setup AML workspace for building, training, and deploying the predictive model in the banking scenario.

1. In the Edge browser, navigate to Azure Portal at
`https://portal.azure.com` and Sign In using your Azure user credentials (provided in the Resources section).

2. Click on Cloud shell and select **Bash**.

    ![](./media/image1.png)

3. Select **No storage account** **required** radio button , select **your Azure subscription** and then click on **Apply**.

    ![](./media/image2.png)

4. We will clone the repo containing the files required to deploy the solution.
   +++git clone https://github.com/technofocus-pte/MLOps-Driven-Chatbot-with-Azure-AI-AML-and-Azure-AI-Search-Integration.git+++

    ![](./media/image3.png)


5. We will also install Python dependencies (e.g. azureml-sdk). Run +++pip install azureml-sdk+++ to install the dependencies.

    ![](./media/image4.png)

6. Lets now run this script to create thre required resources in an Azure resource group within the assigned subscription. 

    +++cd MLOps-Driven-Chatbot-with-Azure-AI-AML-and-Azure-AI-Search-Integration/scripts/+++

    +++chmod +x setup.sh+++
7. Run below setup script now by executing this command. This script will register the Machine Learning resource providers, create an Azure Machine Learning workspace, a compute instance and a compute cluster in AML workspace.
    +++./setup.sh+++

    ![](./media/image5.png)

8. Wait for the script to complete. It takes 4-5 minutes for the script to run.


    ![](./media/image6.png)

    ![](./media/image7.png)


9. Close the **Cloud shell** and click on **Resource group** tile.

    ![](./media/image8.png)

10. Click on your resource group name. 

    ![](./media/image9.png)

11. Explore the details pane to ensure all the resources including an AML workspace, a storage account, a Key vault and a Log Analaytics workspace are created successfully.

12. Click on **Azure Machine Learning workspace** name. Click on **Launch Studio** button. The AML Studio is launched in a new browser tab.


    ![](./media/image17.png)

13. Navigate to the Azure AI Machine Learning Studio tab that already has your workspace opened.
14. Click on **Compute** (in the **Manage** section) from the left navigation menu, to verify that a Compute instance is already **Running**.

    ![](./media/image19.png)

15. Now click on **Compute clusters** from the top menu (next to **Compute instances**), to verify that a compute cluster was successfully deployed.

    ![](./media/image20.png)


>#### **Summary:** In this this task, we successfully created an Azure Machine Learning workspace and configured compute resources, which will be used for training and deploying machine learning models. These foundational steps ensure that we have a secure, scalable environment in place to support the bank's data science and marketing initiatives.


### **Task 2 : Configure Role Assignments**

> We need to configure appropriate Role Assignments on the resource group for your user Azure account in order to be able to index and enrich the customer data, and to be able to create OpenAI services in the AML workspace.

1. Switch back to **Azure portal** home page and click on **Resource group** tile.

    ![](./media/image21.png)

2. Click on your resource group name.

    ![](./media/image22.png)

3. Click on **Access control(IAM)** from left navigation menu, select **Add - > Add role assignment.**

    ![](./media/image23.png)

4. Search for `AzureML Compute Operator` and select it. Click on
    **Next** .

    ![](./media/image24.png)

5. Select **Users, group or service principal** radio button, click on **Select members** hyper link. Search for your **aoaitfsXXXX**
    (search for your logged in AOAI user credentials username as provided in the Resources section of the Lab environment) select it. Finally, click on **Select** button

    ![](./media/image25.png)

6. Click on **Next**.

    ![](./media/image26.png)

7. Click on **Review + assign** now.

    ![](./media/image27.png)

8.  After role assignments are successful, click on **Add -> Add role
    assignment**.

    ![](./media/image28.png)

9.  Repeat Steps 3-8 above, to also add the following role assignments for your logged in user account:

    `Search Index Data Reader`

    `Cognitive Services Contributor`

    `Cognitive Services OpenAI User`

    `Search Service Contributor`

    ![](./media/image29.png)

    ![](./media/image30.png)

    ![](./media/image31.png)

    ![](./media/image32.png)


21. In the IAM details pane, Click on **Role assignments** (next to **Check Access**).

    ![](./media/image34.png)

22. You should be able to see all the assigned roles to your tenant.

    ![](./media/image35.png)

### **Task 3 : Upload Contoso Bank loan documents into Azure Storage account**

When you create an Azure Machine Learning workspace, an Azure Storage Account is created automatically, and connected to your AML workspace. In this task, we will upload Contoso Bank's customer loan documents in the Azure Storage Account. Information in these files will be used to ground the search performed by AI models to answer customer queries in the chat app built later in the lab.

1.  In **Azure portal- > Resource group** , click on your Storage account name

    ![](./media/image36.png)

2.  Select **Configuration** under **Settings**. Then set **Allow Blob anonymous access** to **Enabled** and then click **Save**.

    ![](./media/image37.png)


3.  Click on **Containers** under **Data storage** and click **azureml-blobstore-XXXXXXXXXXXXX** container.

    ![](./media/image38.png)

4.  Click on **Upload -> Browse for files** . select and upload the following files from **C:\Labfiles\Resources** folder in your lab VM:
    - Contoso Bank Home loan FAQS.pdf
    - Contoso Bank Home loan Guide.pdf
    - Contoso Personal Loan FAQs.pdf
    - Contoso Personal Loan guide.pdf
    - enriched_data.csv

    ![](./media/image39.png)

5.  Click on **Upload**

    ![](./media/image40.png)

    ![](./media/image41.png)

>#### **Summary:** In this exercise, we successfully created an Azure Machine Learning workspace and configured compute resources, which will be used for training and deploying machine learning models with required permissions to perform the tasks. These foundational steps ensure that we have a secure, scalable environment in place to support Contoso Bank's data science and marketing initiatives.
