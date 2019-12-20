# MindSphere App Demo

## Description

Small Cloud Foundry-hosted demo application, which can be used in Siemens MindSphere.

The application reads the time series data from the MindSphere's **IoT Time Series Service**, and then plots a simple line chart.

## Dependencies

The application uses [flask](https://pypi.org/project/Flask/), [requests](https://pypi.org/project/requests/), and [plotly](https://pypi.org/project/plotly/) packages.

## Prerequisites

In order to deploy application to Cloud Foundry and MindSphere you need

* MindSphere user account on a developer tenant
* Cloud Foundry Command Line Interface (CF CLI)
* A Cloud Foundry role, which allows to push applications, e.g. *SpaceDeveloper*
* A MindSphere developer role, either *mdsp:core:Developer* or *mdsp:core:DeveloperAdmin*
* An asset in MindSphere

## Usage

First, create aspect and asset in the MindSphere. The name of the aspect and ID of the asset is used in the application.

Next, make following changes to the code:
* In Python file **application**, replace the values of the **ASSET_ID** and **ASPECT** variables
* In manifest file, replace the **appName** with the name of your app, and the **tenant** with the name of your tenant

After these changes, the source code is ready to be deployed into Cloud Foundry.

Please see the MindSphere online [documentation](https://developer.mindsphere.io/howto/howto-cf-running-app.html) how to deploy a Cloud Foundry-hosted application.

## Docs

**Docs** folder contains basic instructions (in Finnish) how to use Siemens MindSphere. There are also two sample applications in the folder.

## Additional Information.

This application has been made as a part of the "Automation in Network" project.