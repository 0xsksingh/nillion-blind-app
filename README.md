# Secure Financial Health Calculator

> A privacy-preserving financial assessment system powered by Nillion's secure computation technology

## Problem Statement
Traditional financial health assessment tools require users to share sensitive financial data with multiple parties (advisors, institutions, regulators), creating privacy risks and potential data breaches. Users need a way to get comprehensive financial guidance while keeping their data private.

## Solution
The Secure Financial Health Calculator uses Nillion's secure computation to process sensitive financial data while maintaining complete privacy. It enables multi-party computation where different stakeholders (users, advisors, regulators) can receive tailored insights without accessing the underlying data.

## Features

### 1. Comprehensive Financial Assessment
- Debt-to-income ratio calculation
- Savings ratio analysis
- Disposable income tracking
- Emergency fund adequacy check
- Credit score impact assessment
- Age-based risk profiling

### 2. Risk Analysis
- Multi-factor risk scoring system
- Weighted risk calculations (40% debt, 30% age, 30% credit)
- Dynamic risk thresholds
- Age-appropriate risk assessments

### 3. Investment Recommendations
- Age-based asset allocation
- Conservative vs aggressive portfolio suggestions
- Safe asset allocation recommendations
- Risk-adjusted investment strategies

### 4. Privacy-Preserving Multi-Party Access
- **Users**: Full access to all financial metrics and recommendations
- **Financial Advisors**: Access to client risk profiles and key ratios
- **Regulators**: Limited access to essential compliance metrics

### 5. Scoring System
- Base score of 100 points
- Dynamic penalty system:
  - Severe penalties (50 points)
  - Moderate penalties (30 points)
  - Minor penalties (15 points)
- Bonus points for good financial habits (20 points)

## Technical Architecture

### Core Components

#### 1. Authentication System

app/components/Login.tsx

- Secure user authentication with cryptographic keys
- Session management
- Role-based access control

#### 2. Computation Engine

app/components/Compute.tsx

- Secure multi-party computation
- Encrypted data processing
- Privacy-preserving calculations

#### 3. Data Storage & Retrieval

app/components/StoreValue.tsx


- Secure value storage with TTL
- Encrypted data persistence
- Secure retrieval mechanisms

#### 4. Result Processing

app/components/ComputeOutput.tsx


- Secure output handling
- Role-specific result filtering
- Data transformation and display

### Security Features

#### 1. Data Protection
- End-to-end encryption
- Zero-knowledge computation
- Secure key management

app/components/Login.tsx


#### 2. Access Control
- Party-specific bindings
- Role-based permissions
- Granular output control

app/components/Compute.tsx


### Implementation Details

#### 1. Input Processing

app/components/Compute.tsx

- Secure integer creation
- Input validation
- Type safety

#### 2. Program Management

app/components/StoreProgram.tsx

- Program storage
- Version control
- Execution management

## Getting Started

### Prerequisites
- Node.js 16+
- nillion-devnet running

### Installation

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

Then follow the rest of the instructions from the Quickstart guide [here.](https://github.com/NillionNetwork/awesome-nillion/issues/2)


## Usage Guide

1. Authentication
   - Login with secure credentials
   - Maintain session security
   - Handle role-based access

2. Data Input
   - Enter financial metrics
   - Validate input data
   - Secure data transmission

3. Computation
   - Process encrypted data
   - Generate secure results
   - Handle multi-party access

4. Result Retrieval
   - Fetch computation results
   - Process role-specific outputs
   - Display filtered information

## Security Considerations

1. Data Privacy
   - All computations performed on encrypted data
   - Zero-knowledge proof verification
   - Secure multi-party computation

2. Access Control
   - Role-based permissions
   - Party-specific data access
   - Granular output control

3. Key Management
   - Secure key generation
   - Safe storage practices
   - Regular key rotation

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Support
For support, please reach out on [Github Discussions](https://github.com/orgs/NillionNetwork/discussions)
```