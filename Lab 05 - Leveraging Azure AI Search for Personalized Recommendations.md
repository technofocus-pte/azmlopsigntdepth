### **Lab 05 -Leveraging Azure AI Search for Personalized Recommendations**


**In this lab you will learn how-to:**

- Use Azure AI Search Services to enrich the chatbot's search capabilities
- Use Azure AI Bot Service for customer engagement using a chatbot


>**Introduction:** In this task, we will leverage Azure AI Search to power personalized recommendations for customers. Azure AI Search allows us to index and analyze customer data, enabling us to recommend relevant loan products based on individual customer preferences and behaviors. We will integrate this search functionality with Contoso Bank’s existing systems to ensure seamless data flow and accurate recommendations.


### **Task 1: Access and Explore the Chatapp.**

In this task, we explore the chat-app

1.  Go back Azure Portal Home page. Search for `App Services` and select it from the drop-down as shown in the below image.

    ![](./media/image150.png)

2.  Click on the your App name thats running.

    ![](./media/image151.png)

3.  Expand **Settings** and select **Environmental variables**. Type `Search` in the search bar to list  Azure AI Search services. In order to make sure all the variables are updated correctly. Click on **AZURE_SEARCH_KEY.**

    ![](./media/image152.png)

4.  Get the key value you saved for this Key in your note pad earlier or copy from your Setup Azure AI Search service task ( Resource group- > Azure AI search service- > Settings- > Keys -> Key 1). Enter the key in the Value field and then click on **Apply**.

    ![](./media/image153.png)

5.  Click on **Add** now to add the AML model endpoint value.

    ![](./media/image154.png)

6.  Go back to **AML Studio tab -> Assets -> Endpoints -> finance-service**. Copy the REST endpoint value.

    ![](./media/image155.png)

    ![](./media/image156.png)

7.  Switch back to the App service tab, Enter the below values, and then click on  **Apply**.

    - Name: `AML_ENDPOINT`

    - Value: Your AML REST endpoint value.

    ![](./media/image157.png)

8.  Click on **Apply** and **confirm** changes on the **Environment Variables** page.

    ![](./media/image158.png)

      
10. From the collapsible left menu under **Settings**, select **Authentication**. **Delete** the existing Identity provider
    and confirm the deletion.

     ![](./media/image159.png)

    

12. Click on **Add identity provider**.

    ![](./media/image160.png)

13. Select Microsoft as the Identity provider, update Name as `MSIdproverXXXX` (replce XXXX with a unique set of number). Select **Client secret expiration** duration as 90 days and then click **Next: Permissions**.

    ![](./media/image161.png)

    

14. Click on **Add permission**. Scroll down in the list to expand **Application** and select **Application.ReadWrite.All**. Then click on **Update permission.**

    ![](./media/image162.png)

    
15. Click on **Add** now.

    ![](./media/image163.png)

    ![](./media/image164.png)

16.  Click on **Overview** page of the app. Wait for the page to load and then click on **Restart**. Confirm restart by clicking on **Yes**.

   ![](./media/image165.png)

17. Click on **Overview** and then click on **Browse** in the top menu.

    ![](./media/image166.png)

18. The app opens in a new tab. Review and **Accept** to allow permissions.

    ![](./media/image167.png)

19. The app opens, enter the below prompts, and explore it.

    `List high-value customers`

    `give customer details whose mortgage is not 0`

    ![](./media/image168.png)

    ![](./media/image169.png)
