### **Lab 04 - Integrating Azure OpenAI service and AI service for Customer Engagement**


**In this lab you will learn how-to:**

- Use AI-based recommendation systems for prediction
- Using insights from the enhanced segmentation
- Use Azure AI Search Services to enrich the chatbot with search

>**Introduction:** In this task, we will integrate the Azure OpenAI chatbot into Contoso Bank’s customer engagement platforms. The chatbot will serve as an interactive tool for customers, helping them explore loan products, get personalized loan recommendations, and receive real-time assistance. We will use Azure OpenAI’s natural language processing capabilities to ensure the chatbot delivers a smooth, human-like experience while collecting valuable customer data for further analysis.

### **Task 1 : Set Up Azure AI Search service**

In this task, we create Azure AI Search service for enriching the chatbot with search and query capabilities based on customer data and loan details.

1.  Switch back to Azure portal and search for `Azure AI search` and select it.

    ![](./media/image85.png)

2.  Click on **Create**.

    ![](./media/image86.png)

3.  Select below values and then click on **Review + Create**.

    - Subscription : Your Azure subscription.

    - Resource group - Select your existing resource group

    - Service name - `cbsb-aisearchXXXX` ( replace XXXX with unique number)

    - Location : **west us**/north Europe /location near to you

    ![](./media/image87.png)

4.  Click on **Create** now.

    ![](./media/image88.png)

5.  Wait for the deployment and then click on **Go to resource**.

    ![](./media/image89.png)

6.  Open a Notepad and make a note of URL value as  **AZURE_SEARCH_ENDPOINT**. We will use it later to communicate to the service.

    ![](./media/image90.png)

7.  Navigate to the **Keys** section (exapnd **Settings**). Copy the API Key (Primary admin key) and save it as **AZURE_SEARCH_KEY** in your notepad. You will need this later to communicate with the service.

    ![](./media/image91.png)

### **Task 2 : Create Azure AI multi-service resource**

In this task, we will create an AI multi-service resource for NLP to enrich data and interact with customers through the chat app.

1.  Follow the steps below to create an Azure AI multi-service resource in the **same region (location) as that of your Azure search service**.

2.  Open a new tab in a browser and go to  `https://portal.azure.com/#create/Microsoft.CognitiveServicesAllInOne`
    Sign in with your Azure subscription account

3.  Enter below values and then click on **Review + create**.

    - Subscription : Your Azure subscription

    - Resource group : Your existing resource group

    - Region : **Same region as your Search service region**

    - Name : `cbsb-aimultiserviceXXXX` (XXXX can be unique number)

    - Price tier : **Standard S0**

    - Select **By checking this box I acknowledge that I have read and understood all the terms below** check box.

    ![](./media/image92.png)

    ![](./media/image93.png)

4.  Review the details and click on **Create**.

    ![](./media/image94.png)

5.  Wait for the deployment to be completed. Deployment takes 1-2 min.
    Click on **Go to resource** button.

    ![](./media/image95.png)

6.  Select **Keys and Endpoint** under the **Resource Management** in the left navigation menu. Make a note of the **Key 1** value as **AZURE_MULTISERVICE_ENDPOINT** in the notepad, as these will be used later in the lab to communicate with this service.

    ![](./media/image96.png)

### **Task 3 : Create Azure OpenAI resource**

In this task, we will create Azure OpenAI resource to deploy OpenAI models for embeddings and completions to use them in our Chat app

1.  Navigate to Azure Portal in a new tab and search for `Azure OpenAI` service and select it.

    ![](./media/image97.png)

2.  Click on **Create** button in the top menu.

    ![](./media/image98.png)

3.  Enter below details and click on

    - Subscription : Azure subscription

    - Resource group -  your Azure resource group

    - Region : **East US**

    - Name -  `cbazopenaiXXXX` (XXXX can be unique number)

    - Price tier -**Standard S0**

    ![](./media/image99.png)

4.  Click on **Next- > Next- > Create** slelecting the default settings.

    ![](./media/image100.png)

    ![](./media/image101.png)

    ![](./media/image102.png)

5.  Once the deployment completes, click on **Go to resource**.

    ![](./media/image103.png)

6.  Expand Resource management from left navigation ,click on **Keys and  Endpoint**. Copy URL in the **Endpoint** field and save in your notepad as **AZURE_OPENAI_ENDPOINT**.
    Copy the **Key 1** value and save as **AZURE_OPENAI_KEY**. 

    ![](./media/image104.png)

7.  Click on **Overview** tab on the left navigation panel, and then click on **Go to Azure OpenAI Studio**. Azure OpenAI Studio opens in new tab.
  
8.  Sign in if required. Close the pop-ups that appear.

    ![](./media/image106.png)

9.  Click on **Deployment** from left navigation menu. In the **Deploy model** drop down menu select **Deploy base model.**

    ![](./media/image107.png)

10. Search for `gpt-35-turbo-16k` and select it. Click on **Confirm**. GPT-3.5 models can understand and generate natural language or code. GPT-3.5 Turbo is the most capable and cost effective model in the GPT-3.5 family, which has been optimized for chat and works well for traditional completions tasks as well.

    ![](./media/image108.png)

11. In the deployment dialogbox, click on **Customize** button

    ![](./media/image109.png)

12. Set **Tokens per Minute Rate limit** to max and then click on **Deploy**.

    ![](./media/image110.png)

13. Repeat above steps and deploy `text-embedding-ada-002` model as well. Text-embedding-ada-002 outperforms all the earlier embedding models on text search, code search, and sentence similarity tasks and gets comparable performance on text classification. Embeddings are numerical representations of concepts converted to number sequences, which make it easy for computers to understand the relationships between those concepts.

    ![](./media/image111.png)

    ![](./media/image112.png)

14. Set maximum **Tokens per Minute Rate Limit** and then click on **Deploy.**

    ![](./media/image113.png)

    ![](./media/image114.png)


### **Task 4 : Add a data source to Azure AI search service**

In this task, we will add our Azure storage container as the data source for all our resources that will be used to enrich data.

1.  Switch back to **Azure portal -> Resource group- > Azure AI search service.**

    ![](./media/image115.png)

2.  Click on **Search management -> Data source** . Select **Add data source -> Add data source.**

    ![](./media/image116.png)

3.  Select the below values and then click on **Create.**

    - Data source: Azure blob Storage

    - Name: unique name (eg: `enrichdatasource`)

    - Subscription: your Azure subscription

    - Storage account- your Azure storage account

    - Blob container -  `azureml-blobstore-XXXX` (your default blob container where raw data is uploaded.)
    - Blob Folder - (Leave blank)

    ![](./media/image117.png)

    ![](./media/image118.png)

### **Task 5: Create skillsets in Azure AI search**

In this task, we will create a skillset  object in Azure AI Search that's attached to an indexer.It contains one or more skills that call built-in AI or external custom processing over documents retrieved from an external data source. Creating and mappink the skills will enhance the in saerch we perform on the index.

1. On the **Identity** page of your Azure AI search service, turn on **System assigned** Managed Identity. Click **Save** on the top menu to generate the Object ID of the managed identity.

    ![](./media/image198.png)

2. Click on **yes**

    ![](./media/image199.png)

3. Copy the **Object ID** of the managed identity created, and click on **Azure Role Assignments** button to assign the required permissions to this ID.

    ![](./media/image200.png)

3. Click on **Add role assignments (Preview)** on the top menu.

    ![](./media/image201.png)

4. Select below values.

    - In the **Scope** drop down, select **Storage**.
    - In the **Resource** drop down, select your storage account.
    - Search and assign the `Storage Blob Data Reader` role to this Managed Identity on your Azure storage.

    ![](./media/image202.png)

5. Click on **Save** now.

    ![](./media/image203.png)

    ![](./media/image204.png)

7. On the Overview page of your Azure Search service, click on **Import data** from the top menu.

    ![](./media/image119.png)

8.  Keep **Existing data source** selected from the **Data Source** drop down, and select **enrichdatasourceXXXX** (your data source). Then click on **Next: Add cognitive skills (Optional)**.

    ![](./media/image120.png)

9.  Expand **Attach AI Services** and select the AI multi-service resource created in the previous task.

    ![](./media/image121.png)

10.  Expand **Add enrichments**, keep default skillset name, check **enable OCR** and select all **checked items requiring a filed name** except
    **Extract personally identifiable information** then click on **Next: Customize target index.**

     ![](./media/image121.png)

11.  Enter Index name as - `customer-index`, and click on **Add field** on top of the field table.

     ![](./media/image123.png)

12.  In the new field row that gets added at the bottm of the table, enter **Field name** as : `customer_id`, select type="Edm.String" and select all skills

     ![](./media/image124.png)

13.  Repeat the above 2 steps to also add the below fields and then click **Next: Create an indexer**

<<<<<<< HEAD
     - Field name -  `customer_name` , Type - Edm.String , Skills -All

     - Field name -  `CustomerSince` , Type - Edm.Int32 , Skills -All

     - Field name -  `campaign_result` , Type - Edm.String , Skills -All

     - Field name -  `age` , Type - Edm.Int32 , Skills -Al
=======
        - Field name -  `customer_name` , Type - Edm.String , Skills -All

        - Field name -  `CustomerSince` , Type - Edm.Int32 , Skills -All

        - Field name -  `campaign_result` , Type - Edm.String , Skills -All

        - Field name -  `age` , Type - Edm.Int32 , Skills -Al
>>>>>>> 41c3d8c6aa4500268ec73b5342a41cfbf99b3a14

    
     ![](./media/image125.png)

14.  Enter the indexer name : `customer-azureblob-indexer` and click **Submit** for the skills to be created.

     ![](./media/image126.png)

     ![](./media/image127.png)

15.  Click on **Indexers** under **Search management**, you should see new indexer with succeeded documents count.

     ![](./media/image128.png)

16.  Click on **Indexes**. Note the new **customer-index** created. Wait for the Vector index size to update.

     ![](./media/image129.png)

### **Task 6: Build and Deploy Chat app in Azure AI Studio.**

In this task, we will create, configure, and deploy the chatbot powered by Azure AI, integrated with our AML model.

1.  Open a new tab, navigate to `https://ai.azure.com` and sign in with your assigned Azure account.

    ![](./media/image131.png)

2.  Click on **New project.**

    ![](./media/image132.png)

3.  Enter the unique project name(`cbsbaoai-proj`) and then click on Create a new hub link on the Hub drop down link as shown below
    image.

    ![](./media/image133.png)

4.  Enter the below values and then click on **Next**

    - Hub name: `cbcbaoaihub`

    - Subscription: Your Azure subscription

    - Resource group - your existing resource group

    - Location -same location (region) as your Azure Open AI service region

    - Connect Azure AI Services or Azure OpenAI: Select your Azure OpenAI service

    - Connect Azure AI Search: Select your Azure AI Search

    ![](./media/image134.png)

5.  Review the details and then click on **Create a project** button. Wait until the project creation finishes.

    ![](./media/image135.png)

    ![](./media/image136.png)

6.  Click on **Chat** from the left navigation menu under **Project Playground**. In Setup section in the details pane, expand **Add your data** and then click on **Add a new data source**.

    ![](./media/image137.png)

7.  Select **Azure AI Search** as **Data source** and then click **Next**.

    ![](./media/image138.png)

8.  Select your **Azure AI Search** service from the drop-down menu, and then select **customer-index** that you created previusly, and then click **Next**.

    ![](./media/image139.png)

9.  In the **Vector Index**, keep the default value (customer-index), click **Next**.

    ![](./media/image140.png)

10. Click on **Create Vector Index**.

    ![](./media/image141.png)

    ![](./media/image142.png)

11. Enter the below prompt in the **Type user query here** text box and press the send button.

    `Details of Customer ID- 3`

    ![](./media/image143.png)

12. Once response is received, enter the below prompt next and press send

    `List high-value customers`

    ![](./media/image144.png)

    ![](./media/image145.png)

13. Now, you are ready to deploy your app. Click on **Deploy- > as a web app** from the top menu.

    ![](./media/image146.png)

14. Enter the below details and then click on **Deploy**. Deployment takes 5-10 min to complete.

    - Select **Create a new web app** radio button

    - Name: should be a unique name (eg `mlappchatappXXXX` - XXXX can be a unique number)

    - Subscription: Your Azure subscription

    - Resource group - your resource existing resource group

    - Location - West US / East US/East US 2 ( usually East US has high demand and deployment may fail). You can use the same location as the hub

    - Pricing plan: Standard (S1) /S2

    ![](./media/image147.png)

    ![](./media/image148.png)

    ![](./media/image149.png)

>**Summary:** We have successfully integrated the Azure OpenAI chatbot into Contoso Bank’s customer engagement platform. The chatbot provides real-time assistance to potential borrowers, enhancing digital engagement and improving the customer experience. This integration allows the bank to deliver personalized recommendations based on customer behavior and preferences, further supporting targeted marketing efforts.


